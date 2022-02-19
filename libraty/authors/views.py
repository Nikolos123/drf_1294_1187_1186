from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book,Biography
from .serializers import AuthorModelSerializer,BiographyModelSerializer,BookModelSerializer

class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

# Create your models here.
# @renderer_classes([JSONRenderer])
class AuthorModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    permission_classes = [IsAdminUser]


class BiographyModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer

class BookModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer