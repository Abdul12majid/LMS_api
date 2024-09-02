from rest_framework import serializers
from .models import Book

class Book_serializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id', 'book_name', 'author', 'status', 'category', 'description',)