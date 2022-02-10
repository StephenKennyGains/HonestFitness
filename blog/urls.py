""" Sets the URLS for the views created in Views.py matching to templates """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostGeneral.as_view(), name='home'),
    path('<slug:slug>/', views.PostFullView.as_view(), name='post_full_view'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path("delete_comment/<int:id>", views.PostFullView.delete_comment, name="delete_comment"),
]
