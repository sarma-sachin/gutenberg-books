from rest_framework import serializers
from .models import BooksAuthor, BooksBook, BooksSubject


class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = "__all__"


class FilterSerializer(serializers.Serializer):
    book_id = serializers.CharField(required=False)
    language = serializers.CharField(required=False)
    mime_type = serializers.CharField(required=False)
    topic = serializers.CharField(required=False)
    author = serializers.CharField(required=False)
    title = serializers.CharField(required=False)


class OutputSerializer(serializers.Serializer):
    title = serializers.CharField()
    language = serializers.CharField()
    subjects = serializers.CharField()


class BooksSerializer(serializers.ModelSerializer):
    language = serializers.CharField()
    subjects = serializers.ListField(child=serializers.CharField())
    bookshelves = serializers.ListField(child=serializers.CharField())
    urls = serializers.ListField(child=serializers.CharField())
    # author = BooksAuthorSerializer(source="author")
    author = serializers.CharField()

    class Meta:
        model = BooksBook
        fields = [
            "id",
            "title",
            "language",
            "author",
            "subjects",
            "bookshelves",
            "urls",
        ]
