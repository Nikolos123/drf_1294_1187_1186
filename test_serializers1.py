import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from test_models import Author


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

    def create(self, validated_data):
        return Author(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        return instance

    def validate_birthday_year(self, value):
        if value < 5:
            raise serializers.ValidationError('Год рождения не может быть отрицательным')
        return value

    def validate(self, attrs):
        if attrs['name'] == 'Толстой' and attrs['birthday_year'] != 1828:
            raise serializers.ValidationError('Неверный год рождения Толстого')
        return attrs


def start():
    author = Author('Толстой', 1828)
    serializer = AuthorSerializer(author)

    renderer = JSONRenderer()
    json_bytes = renderer.render(serializer.data)

    stream = io.BytesIO(json_bytes)
    data = JSONParser().parse(stream)

    serializer = AuthorSerializer(data=data)
    serializer.is_valid()
    # Продолжение скрипта №1

    # Создание
    author = serializer.save()
    print(type(author))
    print(author)

    # Обновление всех данных
    data = {'name': 'Пушкин', 'birthday_year': 1880}
    serializer = AuthorSerializer(author, data=data)
    serializer.is_valid()
    author = serializer.save()
    print(author)

    #Обновление частичное
    data = {'birthday_year': 10}
    serializer = AuthorSerializer(author, data=data, partial=True)
    serializer.is_valid()
    author = serializer.save()
    print(f'{author} {author.birthday_year}')


    # Проверка 1го поля
    data = {'birthday_year': 1}
    serializer = AuthorSerializer(author, data=data, partial=True)
    if  serializer.is_valid():
        author = serializer.save()
        print(f'{author} {author.birthday_year}')
    else:
        print(serializer.errors)

    # Проверка всех полей
    data = {'name': 'Толстой', 'birthday_year': 2000}
    serializer = AuthorSerializer(author, data=data)
    if serializer.is_valid():
        author = serializer.save()
        print(author)
    else:
        print(serializer.errors)


start()