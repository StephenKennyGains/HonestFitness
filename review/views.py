""" Views allow for models to be displayed to the user and
are displayed by referencing them through the templates.
Below are the views to allow users to enter into a full view
of listed postsand comment on them and like them if registered
and logged in"""

from django.shortcuts import render
from django.views import generic, View
from .models import Review
from .forms import ReviewForm

# Create your views here.


class UserReview(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Pagination comes in at 3 posts to scroll earlier posts"""

    model = Review
    queryset = Review.objects.filter(status=1, approved=True).order_by(
            "-created_on")
    template_name = "review.html"


class CreateReview(View):

    """ Validate and create data from forms on review page """

    model = Review
    template_name = "create_review.html"
