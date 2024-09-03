from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import Book_serializer
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class all_books(ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = Book_serializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['category_id']


class book_info(RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = Book_serializer
