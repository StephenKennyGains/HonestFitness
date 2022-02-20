"""The models set the foundation of data that can then
be viewed and edited by admin and users. Below are the
models for reviews, allowing for CRUD functionality.
These models are called on in the view"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

RATING = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5")
)


class Review(models.Model):
    """Review model allows users to post reviews
    of places and people in fitness that they feel
    are worth highlighting"""

    title = models.CharField(max_length=200, unique=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review")
    location = models.CharField(max_length=100, unique=False)
    reviewbody = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING, default=1)

    class Meta:
        """Sets the ordering to be from latest to oldest"""
        ordering = ["-created_on"]

        def __str__(self):
            """Return review name as string"""
            return self.title
