"""The models set the foundation of data that can then
be viewed and edited by admin and users. Below are the
models for blog posts and user comments allowing for
CRUD functionality. These models are called on in the view"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

CATEGORY = (
    (1, "General"),
    (2, "Training Advice"),
    (3, "Exercise Advice")
)


class Post(models.Model):
    """Post model sets the attributes to be included in each
    post and their limitations like title length. Cascade
    is used to ensure asscociated data with a post is also
    deleted when deleted"""

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORY, default=1)

    class Meta:
        """Sets the ordering to be from latest to oldest"""
        ordering = ["-created_on"]

    def __str__(self):
        """Return post name as string"""
        return self.title


class Comment(models.Model):
    """Allows for commenting on blog posts and keeps comments
    specific to the post they referece. Sets the limitations
    and criteria for user commenting."""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Sets the odering from oldest to newest for conversation"""
        ordering = ['created_on']

    def __str__(self):
        return f"User {self.name} says {self.body}"
