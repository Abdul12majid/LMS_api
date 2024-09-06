from rest_framework import serializers
from .models import Book, Category
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError

class Book_serializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.category_name  # Access the name attribute
        return representation

    class Meta:
        model = Book
        fields = ('id', 'book_name', 'author', 'status', 'category', 'description',)


class MySerializer(serializers.Serializer):
    keywords=serializers.CharField(max_length=500)
