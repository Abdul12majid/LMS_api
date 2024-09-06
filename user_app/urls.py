from django.urls import path, include
from . import views

urlpatterns = [
	path("create_user", views.create_user),
    path("login_user", views.login_user),
    path("logout_user", views.logout_user),
]