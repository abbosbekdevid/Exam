from rest_framework import serializers


class AuthorSerializers(serializers.Serializer):
    name = serializers.CharField()
    fname = serializers.CharField()
    date_birth = serializers.DateField()
    country = serializers.CharField()


class BookCategorySerializers(serializers.Serializer):
    name = serializers.CharField()

class BookSerializers(serializers.Serializer):
    title = serializers.CharField()
    page = serializers.IntegerField()
    price = serializers.IntegerField()
    author = AuthorSerializers()
    category = BookCategorySerializers()