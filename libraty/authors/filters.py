
from django_filters import rest_framework as filters
from .models import Book


class BookFilter(filters.FilterSet):
   name = filters.CharFilter(lookup_expr='contains')

   class Meta:
       model = Book
       fields = ['name','id']