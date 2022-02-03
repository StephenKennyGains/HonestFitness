from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review, UserReview
from .forms import ReviewForm

# Create your views here.


class Review(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Pagination comes in at 3 posts to scroll earlier posts"""

    model = Review
    queryset = Review.objects.filter(status=1, approved=True).order_by(
        "-created_on")
    template_name = "review.html"

    def post(self, request, *args, **kwargs):

        """ Sets the display and oredering of approved comments
        and checks for the log in status for display"""

        user_review = get_object_or_404
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.name = request.user.username
            user_review = review_form.save(commit=False)
            user_review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "review.html",
            {
                "user_review": user_review,
                "reviewed": True,
                "review_form": review_form,
            },
        )
