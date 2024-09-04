from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import Book_serializer, MySerializer
from .models import Book
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class all_books(ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = Book_serializer
	filter_backends = [DjangoFilterBackend, SearchFilter]
	search_fields = ['book_name', 'description']
	filterset_fields = ['category_id']


class book_info(RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = Book_serializer


@api_view(['POST', 'GET'])
def find_book(request, pk):
    serializer = MySerializer(data=request.data)

    if serializer.is_valid():
        pk = serializer.validated_data['keywords']
        books = Book.objects.filter(book_name__icontains=pk)
        # Process the found books and return a response
        return Response({'books': books})
    else:
        return Response({'error': serializer.errors}, status=400)