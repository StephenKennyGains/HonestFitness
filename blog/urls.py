from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostListGeneral.as_view(), name='home'),
    path('<slug:slug>/', views.PostFullView.as_view(), name='post_full_view'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
