from django.contrib import admin

# Register your models here.

from .models import Book,Biography,Author

admin.site.register(Book)
admin.site.register(Biography)
admin.site.register(Author)