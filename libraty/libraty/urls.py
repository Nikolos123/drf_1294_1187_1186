"""libraty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter,SimpleRouter

from authors.views import AuthorModelViewSet,BookModelViewSet,BiographyModelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from user.views import UserListAPIView


schema_view = get_schema_view(
    openapi.Info(
        title='Library',
        default_version='v2',
        description='Project',
        contact=openapi.Contact(email='test@mail.ru'),
        license=openapi.License(name='ST License')
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,)

)




router = DefaultRouter()
router.register('authors',AuthorModelViewSet)
router.register('books',BookModelViewSet)
router.register('biography',BiographyModelViewSet)
# router.registry('books',AuthorModelViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include(router.urls,)),
    path('api-token-auth/',obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('swagger/',schema_view.with_ui('swagger')),
    # path('swagger<str:format>',schema_view.without_ui()),
    path('swagger/',schema_view.with_ui('swagger')),
    path('redoc/',schema_view.with_ui('redoc')),
    # path('api/<str:version>/user/',UserListAPIView.as_view()),
    # path('api/user/v1/',include('user.urls',namespace='v1')),
    # path('api/user/v2/',include('user.urls',namespace='v2')),

    path('graphql/',GraphQLView.as_view(graphiql=True)),

]
