from django.urls import path, include
from . import views

urlpatterns = [
    path("books", views.all_books.as_view()),
    path("books/<str:pk>", views.book_info.as_view()),
    path("find_book", views.find_book),
    path("find_book/<str:pk>", views.search),
    path("create_user", views.create_user),
    path("login_user", views.login_user),
    path("logout_user", views.logout_user),
    path("borrow_book/<int:pk>", views.borrow_book),

]
