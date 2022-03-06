from django.urls import path

from user.views import UserListAPIView

app_name = 'user'

urlpatterns = [

    path('', UserListAPIView.as_view()),

]
