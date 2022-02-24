""" Sets the URLS for the views created in Views.py matching to templates """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostGeneral.as_view(), name='home'),
    path('general_posts/', views.ViewMoreGeneral.as_view(),
         name='general_posts'),
    path('advice_posts/', views.ViewMoreTraining.as_view(),
         name='advice_posts'),
    path('exercise_posts/', views.ViewMoreExercise.as_view(),
         name='exercise_posts'),
    path('<slug:slug>/', views.PostFullView.as_view(), name='post_full_view'),
    path('deletecomment/<int:id>',
         views.PostFullView.delete_comment, name='delete_comment'),
]
