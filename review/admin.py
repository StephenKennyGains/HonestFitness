""" Admin.py allows for CRUD functionality for reviews through
an admin panel and enables review and editing of user reviews"""
from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Sets the display and functionality behind reviews """

    list_display = ('reviewbody', 'title', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'review')
