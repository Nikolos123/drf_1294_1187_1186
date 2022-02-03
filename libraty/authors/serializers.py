
from rest_framework.serializers import ModelSerializer

from .models import Author

class AuthorModelSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
        # fields = ('first_name',)
