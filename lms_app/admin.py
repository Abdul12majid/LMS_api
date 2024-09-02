from django.contrib import admin
from .models import Book, Category, Status
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Book)
class book_data(ImportExportModelAdmin):
	pass

admin.site.register(Category)
admin.site.register(Status)