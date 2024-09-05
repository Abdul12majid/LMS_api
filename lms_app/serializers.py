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

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True, max_length=50)
    confirm_password = serializers.CharField(min_length=8, write_only=True, max_length=50)
    

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']

    def validate(self, attrs):

        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError("Passwords do not match")

        email_exists = User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError("Email has been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()