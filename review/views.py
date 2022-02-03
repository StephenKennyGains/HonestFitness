from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Review
from .forms import ReviewForm

# Create your views here.


class Review(generic.ListView):

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
            review = review_form.save(commit=False)
            review.user_name = request.user
            review.save()

        else:
            review_form = ReviewForm()

        return render(
            request, 'review.html')
