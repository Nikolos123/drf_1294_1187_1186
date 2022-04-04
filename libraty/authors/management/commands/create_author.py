from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from authors.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):

        Author.objects.create(first_name='test',last_name='test',birthday_year=1111)
        User.objects.create_superuser(username='nikolay',password='1',email='test@mail.ru')