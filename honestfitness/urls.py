"""honestfitness URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    path('review/', include('review.urls'), name='review_urls'),
    path('manageprofile/', include('manageprofile.urls'), name='manage_profile_urls'),
    path('accounts/', include('allauth.urls')),
]
