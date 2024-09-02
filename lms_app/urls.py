from django.urls import path, include
from . import views

urlpatterns = [
    path("books", views.all_books.as_view()),
    path("books/<str:pk>", views.book_info.as_view()),
]
