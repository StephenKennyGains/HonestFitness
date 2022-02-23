""" Views allow for models to be displayed to the user and
are displayed by referencing them through the templates.
Below are the views to allow users to enter into a full view
of listed posts and comment on them and like them if registered
and logged in"""

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm


class PostGeneral(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Posts limited to 3 most recent for each category """

    context_object_name = "category"
    template_name = "index.html"
    model = Post

    def get_queryset(self):
        myset = {
            "General": Post.objects.filter(status=1, category=1).order_by(
                "-created_on")[:3],
            "Training": Post.objects.filter(status=1, category=2).order_by(
                "-created_on")[:3],
            "Exercise": Post.objects.filter(status=1, category=3).order_by(
                "-created_on")[:3]
        }
        return myset


class ViewMoreGeneral(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Posts limited to 3 most recent for each category """

    context_object_name = "category"
    template_name = "general_posts.html"
    model = Post

    def get_queryset(self):
        myset = {
            "General": Post.objects.filter(status=1, category=1).order_by(
                "-created_on"),
        }
        return myset


class ViewMoreTraining(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Posts limited to 3 most recent for each category """

    context_object_name = "category"
    template_name = "advice_posts.html"
    model = Post

    def get_queryset(self):
        myset = {
            "Training": Post.objects.filter(status=1, category=2).order_by(
                "-created_on"),
        }
        return myset


class PostFullView(View):

    """ Sets the view for posts to be entered into in a new
    template under post_full_view and view approved comments
    and likes """

    def get(self, request, slug, *args, **kwargs):

        """ Displays the current post and comments.
        Comments are connected to the specific post using
        id and slug"""

        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.order_by('created_on')

        return render(
            request,
            "post_full_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        """ Sets the display and functionality to a user
        submitted comment calling on the comment form,
        checking its validity and saving to the database
        to then be displayed"""

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.path_info)
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_full_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )

    def delete_comment(request, id=None):

        """ Allows for comments to be deleted """

        comment = get_object_or_404(Comment, id=id)
        deletion_request = request.user
        if (
            comment.name == deletion_request.username and
            deletion_request.is_authenticated
        ):
            comment.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                f'{"Your comment has been deleted"}',
            )
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
