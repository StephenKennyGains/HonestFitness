from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

RATING = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5")
)


class Review(models.Model):
    """Review moodel allows users to post reviews
    of places and people in fitness that they feel
    are worth highlighting"""

    title = models.CharField(max_length=200, unique=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review")
    location = models.CharField(max_length=100, unique=False)
    reviewbody = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=RATING, default=1)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        """Sets the ordering to be from latest to oldest"""
        ordering = ["-created_on"]

    def __str__(self):
        """Return review name as string"""
        return self.title


class UserReview(models.Model):
    """Review moodel allows users to post reviews
    of places and people in fitness that they feel
    are worth highlighting"""

    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="user_review")
    user_title = models.CharField(max_length=200, unique=False)
    user_location = models.CharField(max_length=100, unique=False)
    user_reviewbody = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user_rating = models.IntegerField(choices=RATING, default=1)
    approved = models.BooleanField(default=False)

    class Meta:
        """Sets the ordering to be from latest to oldest"""
        ordering = ["-created_on"]

    def __str__(self):
        """Return review name as string"""
        return self.user_title
