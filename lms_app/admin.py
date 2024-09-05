from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Book, Category, Status, Profile
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.unregister(Group)

@admin.register(Book)
class book_data(ImportExportModelAdmin):
	pass

class ProfileInline(admin.StackedInline):
	model=Profile

class UserAdmin(admin.ModelAdmin):
	model=User
	fields=('username',)
	inlines=[ProfileInline]

admin.site.register(Category)
admin.site.register(Status)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)