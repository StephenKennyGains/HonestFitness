""" Views allow for models to be displayed to the user and
are displayed by referencing them through the templates.
Below are the views to allow users to enter into a full view
of listed postsand comment on them and like them if registered
and logged in"""

from django.shortcuts import render, get_object_or_404
from django.views import generic
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

    def post(self, request):

        """ Validate and create data from forms on review page """

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            print("FORM IS VALID")
            review = review_form.save(commit=False)
            review.author = request.user
            review.title = request.POST.get('title')
            review.location = request.POST.get('location')
            review.rating = int(request.POST.get('rating'))
            review.save()

        else:
            print("FORM IS NOT VALID")
            review_form = ReviewForm()

        return render(
            request,
            'review.html',
            {
                "reviewed": True,
                "review_form": review_form,
            },
        )
