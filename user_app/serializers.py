from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True, max_length=50)
    

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        email_exists = User.objects.filter(email=attrs['email']).exists()
        if username_exists:
            raise ValidationError("username has been used")
        elif email_exists:
                raise ValidationError("Email has been used")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=500)
    password = serializers.CharField(max_length=500, write_only=True)