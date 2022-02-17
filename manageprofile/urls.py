"""Sets the urls for manageprofile"""
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('deletereview/<int:id>', views.DeleteReviewView.delete_review,
         name='delete_review'),
]
