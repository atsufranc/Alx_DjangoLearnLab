from rest_framework import serializers
from .models import Book    
# Import the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']  # Specify the fields to be serialized   
        