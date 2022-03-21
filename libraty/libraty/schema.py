import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from authors.models import Author,Book



# #level 1
# class Query(ObjectType):
#
#     hello = graphene.String(default_value="Hi!")
#
# schema = graphene.Schema(query=Query)


# #level 2
# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
# class Query(ObjectType):
#
#     authors = graphene.List(AuthorType)
#
#     def resolve_authors(root,info):
#         return Author.objects.all()
#
# schema = graphene.Schema(query=Query)


#
# #level 3
# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
# class Query(ObjectType):
#
#     authors = graphene.List(AuthorType)
#     books = graphene.List(BookType)
#
#     def resolve_authors(root,info):
#         return Author.objects.all()
#
#     def resolve_books(root,info):
#         return Book.objects.all()
#
# schema = graphene.Schema(query=Query)



# #level 4
# class BookType(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = '__all__'
#
# class AuthorType(DjangoObjectType):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#
#
# class Query(ObjectType):
#
#     author_id = graphene.Field(AuthorType,id=graphene.Int())
#
#     def resolve_author_id(root,info,id=None):
#         try:
#             return Author.objects.get(id=id)
#         except Author.DoesNotExist:
#             return None
#
#     books_by_author = graphene.List(BookType,last_name=graphene.String(required=False))
#     def resolve_books_by_author(root,info,last_name=None):
#         books = Book.objects.all()
#         if last_name:
#             books = books.filter(authors__last_name=last_name)
#
#         return books
#
#
#
# schema = graphene.Schema(query=Query)


# level 5
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'



class Query(ObjectType):

    author_id = graphene.Field(AuthorType,id=graphene.Int())

    def resolve_author_id(root,info,id=None):
        try:
            return Author.objects.get(id=id)
        except Author.DoesNotExist:
            return None

    books_by_author = graphene.List(BookType,last_name=graphene.String(required=False))
    def resolve_books_by_author(root,info,last_name=None):
        books = Book.objects.all()
        if last_name:
            books = books.filter(authors__last_name=last_name)

        return books


class AuthorUpdateMutation(graphene.Mutation):

    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls,root,info,birthday_year,id):
        author = Author.objects.get(id=id)
        author.birthday_year = birthday_year
        author.save()
        return AuthorUpdateMutation(author=author)



class AuthorCreateMutation(graphene.Mutation):

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        birthday_year = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls,root,info,first_name,last_name,birthday_year):
        author = Author(first_name=first_name,last_name=last_name,birthday_year=birthday_year)
        author.save()
        return AuthorCreateMutation(author=author)


class AuthorDeleteMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls,root,info,id):
        Author.objects.get(id=id).delete()

        return AuthorDeleteMutation(author=None)


class Mutations(ObjectType):

    update_author = AuthorUpdateMutation.Field()
    create_author = AuthorCreateMutation.Field()
    delete_author = AuthorDeleteMutation.Field()




schema = graphene.Schema(query=Query,mutation=Mutations)