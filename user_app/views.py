from django.shortcuts import render
from .serializers import LoginSerializer, SignUpSerializer, BookSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from lms_app.models import Book, Profile

# Create your views here.

@api_view(['POST', 'GET'])
def create_user(request):
	serializer = SignUpSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		response = {
			"message":"user created successfully",
			"data": serializer.data
			}
		return Response(data=response, status=status.HTTP_201_CREATED)
	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def login_user(request):
	serializer = LoginSerializer(data=request.data)
	if serializer.is_valid():
		username = request.data['username']
		password = request.data['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return Response({'Info': "Login successful"})
		else:
			return Response({'Error': "Incorrect password or username"})
	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def logout_user(request):
	logout(request)
	return Response({'Info': "You've been logged out."})


@login_required(login_url='login-user')
@api_view(['GET'])
def borrowed_books(request):
	user = request.user
	books = user.profile.books_borrowed.all()
	serializer = BookSerializer(books, many=True)
	return Response(data=serializer.data)
