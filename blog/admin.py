""" Admin.py allows for CRUD functionality for blog posts through
an admin panel and enables approval of user commenting on posts"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Review


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

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """ Allows the comments to show if approved """
        queryset.update(approved=True)


@admin.register(Review)
class CommentAdmin(admin.ModelAdmin):
    """ Sets the display and functionality behind review approval """

    list_display = ('review', 'title', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'review')
    actions = ['approve_reviews']

    def approve_comments(self, request, queryset):
        """ Allows the comments to show if approved """
        queryset.update(approved=True)
