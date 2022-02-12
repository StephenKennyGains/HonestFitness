from . import views
from django.urls import path

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('deletereview/<int:id>', views.DeleteReviewView.delete_review, name='delete_review'),
]