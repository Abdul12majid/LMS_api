from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import Book_serializer, MySerializer, SignUpSerializer
from .models import Book, Profile
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class all_books(ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = Book_serializer
	filter_backends = [DjangoFilterBackend, SearchFilter]
	search_fields = ['book_name', 'description']
	filterset_fields = ['category_id']
	pagination_class = PageNumberPagination


class book_info(RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = Book_serializer


@api_view(['POST', 'GET'])
def find_book(request):
	#get_book = Book.objects.filter(book_name__contains=pk)
	serializer = MySerializer(data=request.data)
	if serializer.is_valid():
		keyword = request.data['keywords']
		get_book = Book.objects.filter(book_name__contains=keyword).exists()
		if get_book:
			book_result = Book.objects.filter(book_name__contains=keyword)
			serializer_class = Book_serializer(book_result, many=True)
			print(keyword)
			return Response({'Info':serializer_class.data})
		else:
			return Response({'Info':'Book not found'})	
	return Response({'Info':'input parameters'})


@api_view(['GET'])
def search(request, pk):
	get_book = Book.objects.filter(book_name__contains=pk).exists()
	if get_book:
		print("Found")
		book_result = Book.objects.filter(book_name__contains=pk)
		serializer_class = Book_serializer(book_result, many=True)
		return Response({'Info':serializer_class.data})
	else:
		print("not found")
		return Response({'Info':'Book not found'})
	return Response({'Info':'Search Book'})


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


@api_view(['GET'])
def borrow_book(request, pk):
	user = User.objects.get(id=3)
	get_book = Book.objects.filter(id=pk).exists()
	if get_book:
		the_book = Book.objects.get(id=pk)
		serializer = Book_serializer(the_book)
		add_book = user.profile.books_borrowed.add(the_book)
		user.profile.book_count+=1
		user.profile.save()
		print("Successful")
		return Response({'Borrowed Book':serializer.data})
	else:
		print("not found")
		return Response({'Info':'Book not found'})
	return Response({'Info':'Borrow Book'})