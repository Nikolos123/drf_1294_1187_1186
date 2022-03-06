from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from user.serializers import UserBasedModelSerializer, UserModelSerializer


class UserListAPIView(ListAPIView):

    queryset = User.objects.all()


    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserBasedModelSerializer
        return UserModelSerializer