""" Sets the URLS for the views created in Views.py matching to templates """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostGeneral.as_view(), name='home'),
    path('<slug:slug>/', views.PostFullView.as_view(), name='post_full_view'),
    path('deletecomment/<int:id>',
         views.PostFullView.delete_comment, name='delete_comment'),
]
