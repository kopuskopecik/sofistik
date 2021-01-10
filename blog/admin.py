from django.contrib import admin

from .models import Blog, Category, Tag

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

	list_display = ['title']


class TagAdmin(admin.ModelAdmin):
		
	list_display = ['title']

class BlogAdmin(admin.ModelAdmin):
		
	list_display = ["slug", "title", "category", "user", "active"]
	list_editable = ["title", "category", "user", "active"]



admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)