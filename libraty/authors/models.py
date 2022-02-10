from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.last_name} | {self.first_name} | {self.birthday_year}'


class Biography(models.Model):
    text = models.TextField(null=True,blank=True)
    author = models.OneToOneField(Author,on_delete=models.CASCADE)

class Book(models.Model):
    name = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)