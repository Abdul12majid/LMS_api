from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    book_count = models.IntegerField(default=1)
    #status = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    due_date = models.DateField(null=True, blank=True)
    #borrower = models.ManyToManyField(User, blank=True)
    cover_image = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return self.book_name


class Category(models.Model):
	category_name = models.CharField(max_length=255, null=True, blank=True)
	
	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
        return self.category_name