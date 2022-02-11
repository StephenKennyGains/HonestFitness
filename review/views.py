""" Views allow for models to be displayed to the user and
are displayed by referencing them through the templates.
Below are the views to allow users to enter into a full view
of listed postsand comment on them and like them if registered
and logged in"""

from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic, View
from .models import Review
from .forms import ReviewForm


# Create your views here.


class UserReview(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Pagination comes in at 3 posts to scroll earlier posts"""

    model = Review
    queryset = Review.objects.order_by("-created_on")
    template_name = "review.html"


class CreateReview(View):

    """ Sets the view for posts to display to the homepage.
    Pagination comes in at 3 posts to scroll earlier posts"""

    def get(self, request):

        """ Displays the current post and approved comments.
        Sets the value for the like button to false and queries
        if the user has liked the post so that it can then be
        set to true for display"""

        form = ReviewForm(request.GET or None)
        if request.user.is_authenticated:
            return render(
                request,
                "create_review.html",
                {"form": form, "review_form": ReviewForm()},
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                f' {"Tou must be logged in to submit a review"}',
            )
            return HttpResponseRedirect("reviews.html")

    def post(self, request):

        """ Displays the current post and approved comments.
        Sets the value for the like button to false and queries
        if the user has liked the post so that it can then be
        set to true for display"""

        form = ReviewForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.user = request.user
                post.save()
            return HttpResponseRedirect("review.html")
        context = {
            "form": form,
        }

class EditReview(View):

    """ Allows for reviews to be edited """

    def edit_review(request, id=None):

        """ Allows for Reviews to be edited"""

        review = Review.objects.get(id=id)

        if request.method != "POST":
            form = ReviewForm(instance=review)
        else:
            form = ReviewForm(instance=review, data=request.POST)
            if form.is_valid():
                review = review.save(commit=False)
                review.author = request.user
                review.user = request.user
                form.save()
                return HttpResponseRedirect(reverse("review.html"))

        context = {"review": review, "form": form}
        return render(request, "edit_review.html")
