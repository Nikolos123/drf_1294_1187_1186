class Author:

   def __init__(self, name, birthday_year):
       self.name = name
       self.birthday_year = birthday_year

   def __str__(self):
       return self.name

class Biography:

   def __init__(self, text, author):
       self.author = author
       self.text = text


class Book:

   def __init__(self, name, authors):
       self.name = name
       self.authors = authors
