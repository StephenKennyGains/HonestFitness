from django.contrib import admin
from .models import Review, UserReview

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Sets the display and functionality behind review approval """

    list_display = ('reviewbody', 'title', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'review')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        """ Allows the comments to show if approved """
        queryset.update(approved=True)


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    """ Sets the display and functionality behind review approval """

    list_display = ('user_reviewbody', 'user_title', 'user_rating', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'user_review')
    actions = ['approve_user_reviews']

    def approve_user_reviews(self, request, queryset):
        """ Allows the reviews to show if approved """
        queryset.update(approved=True)
