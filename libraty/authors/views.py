from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book,Biography
from .serializers import AuthorModelSerializer,BiographyModelSerializer,BookModelSerializer

# Create your models here.
# @renderer_classes([JSONRenderer])
class AuthorModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BiographyModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer

class BookModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer