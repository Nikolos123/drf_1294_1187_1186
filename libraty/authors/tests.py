import math
# import os
# from django.core.wsgi import get_wsgi_application
# os.environ['DJANGO_SETTINGS_MODULE'] = 'libraty.settings'
# application = get_wsgi_application()
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory,force_authenticate,APIClient,APISimpleTestCase,APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from authors.views import AuthorModelViewSet
from authors.models import Author,Biography

# import os
# from django.core.wsgi import get_wsgi_application
# os.environ['DJANGO_SETTINGS_MODULE'] = 'libraty.settings'
# application = get_wsgi_application()

class TestAuthorViewSet(TestCase):


    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.email = 'admin_123456789@mail.ru'

        self.data = {'first_name':'Александр','last_name':'Пушкин','birthday_year':1799}
        self.data_put = {'first_name':'Николай','last_name':'Пушкин','birthday_year':1990}
        self.url = '/api/authors/'
        self.admin = User.objects.create_superuser(self.name,self.email,self.password)

    #APIRequestFactory force_authenticate
    def test_get_list(self):
        #
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = AuthorModelViewSet.as_view({'get':'list'})
        response = view(request)
        self.assertEqual(response.status_code ,status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url,self.data,format='json')
        view = AuthorModelViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        force_authenticate(request,self.admin)
        view = AuthorModelViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    #APIClient
    def test_get_detail(self):

        client = APIClient()
        author = Author.objects.create(**self.data)
        response = client.get(f'{self.url}{author.id}/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_put_guest(self):
        client = APIClient()
        author = Author.objects.create(**self.data)
        response = client.put(f'{self.url}{author.id}/',self.data_put)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_put_admin(self):
        client = APIClient()
        author = Author.objects.create(**self.data)
        client.login(username=self.name,password=self.password)
        response = client.put(f'{self.url}{author.id}/', self.data_put)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        author_ = Author.objects.get(id = author.id)
        self.assertEqual(author_.first_name,self.data_put.get('first_name'))
        self.assertEqual(author_.last_name,self.data_put.get('last_name'))
        self.assertEqual(author_.birthday_year,self.data_put.get('birthday_year'))

        client.logout()

    def tearDown(self) -> None:
        pass

    # APISimpleTestCase

class TestMath(APISimpleTestCase):

    def test_sqrt(self):

        self.assertEqual(math.sqrt(4),2)

#APITestCase
class TestBiography(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_123456789'
        self.email = 'admin_123456789@mail.ru'

        self.data = {'first_name':'Александр','last_name':'Пушкин','birthday_year':1799}
        self.data_put = {'first_name':'Николай','last_name':'Пушкин','birthday_year':1990}
        self.url = '/api/biography/'
        self.admin = User.objects.create_superuser(self.name,self.email,self.password)

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_put_admin(self):
        author = Author.objects.create(**self.data)
        bio = Biography.objects.create(text='test',author=author)
        self.client.login(username=self.name,password=self.password)
        response = self.client.put(f'{self.url}{bio.id}/',{'text':'Biography','author':bio.author.id})
        self.assertEqual(response.status_code,status.HTTP_200_OK)


        bio_ =Biography.objects.get(id=bio.id)
        self.assertEqual(bio_.text , 'Biography')
        self.client.logout()

    def test_put_mixer(self):

        bio = mixer.blend(Biography)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'author': bio.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        bio_ = Biography.objects.get(id=bio.id)
        self.assertEqual(bio_.text, 'Biography')
        self.client.logout()

    def test_put_mixer_fields(self):
        bio = mixer.blend(Biography,text='Биография')
        self.assertEqual(bio.text, 'Биография')
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'author': bio.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        bio_ = Biography.objects.get(id=bio.id)
        self.assertEqual(bio_.text, 'Biography')
        self.client.logout()
