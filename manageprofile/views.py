from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from review.models import Review


# Create your views here.


@login_required
def profile(request, pk=None):
    """
    Allows connection of content to user
    """
    if pk:
        review_author_id = get_object_or_404(User, pk=pk)
        author_id_reviews = Review.objects.filter(author_id=request.user)

    else:
        review_author_id = request.user
        author_id_reviews = Review.objects.filter(author_id=request.user)
    return render(
        request,
        "profile.html",
        {
            "review_author_id": review_author_id,
            "author_id_reviews": author_id_reviews
        },
    )


@login_required
class DeleteReviewView(DeleteView):

    """ Finds reviews related to the user for the option
    to then delete their reviews """

    def delete_review(request, id=None):

        """ Attaches the delete function to the
        specific review related to the user """

        review_delete = Review.objects.get(id=id)
        review_delete.delete()
        messages.error(request,
                        "Deletion Completion!")
        return HttpResponseRedirect(reverse("profile"))
