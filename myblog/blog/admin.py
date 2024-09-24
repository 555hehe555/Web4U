from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")


@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_comments')
