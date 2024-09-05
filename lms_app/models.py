from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
	category_name = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_name

class Status(models.Model):
	status_name = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		verbose_name_plural = 'Status'

	def __str__(self):
		return self.status_name


class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField(default=datetime.now())
    genre = models.CharField(max_length=100)
    book_count = models.IntegerField(default=1)
    borrower = models.ManyToManyField(User, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    due_date = models.DateField(null=True, blank=True)
    cover_image = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.book_name


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    books_borrowed = models.ManyToManyField(Book, related_name='borrowed_books', symmetrical=False, blank=True)
    date_modified=models.DateTimeField(auto_now=True)
    profile_image = models.URLField(null=True, blank=True)
    profile_bio=models.CharField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)