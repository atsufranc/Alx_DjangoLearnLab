from rest_framework import serializers
from .models import Author, Book

# BookSerializer serializes all fields of the Book model.
# Includes custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer serializes the name and includes a nested list of books using BookSerializer.
# Demonstrates handling of nested relationships between Author and Book.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

# The relationship between Author and Book is handled via the 'books' related_name in the Book model's ForeignKey.
# This allows AuthorSerializer to dynamically include all books for each author.
