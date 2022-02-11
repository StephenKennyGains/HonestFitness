""" Admin.py allows for CRUD functionality for blog posts through
an admin panel and enables approval of user commenting on posts"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """ Sets the display and functionality for blog posting """

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Sets the display and functionality behind comment approval """

    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'body')
