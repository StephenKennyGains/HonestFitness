""" Sets the URLS for the views created in Views.py matching to templates """

from django.urls import path
from . import views


urlpatterns = [
        path('review/', views.Review.as_view(), name='review'),
        path('create_review/',
             views.CreateReview.as_view(), name='create_review'),
]
