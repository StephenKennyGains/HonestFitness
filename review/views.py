from django.views import generic
from .models import Review

# Create your views here.


class Review(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Pagination comes in at 3 posts to scroll earlier posts"""

    model = Review
    queryset = Review.objects.filter(status=1).order_by(
        "-created_on")
    template_name = "review.html"
