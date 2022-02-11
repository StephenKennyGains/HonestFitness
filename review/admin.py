""" Admin.py allows for CRUD functionality for reviews through
an admin panel and enables review and approval of user reviews"""
from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Sets the display and functionality behind review approval """

    list_display = ('reviewbody', 'title', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'review')
