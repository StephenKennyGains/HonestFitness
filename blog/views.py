""" Views allow for models to be displayed to the user and
are displayed by referencing them through the templates.
Below are the views to allow users to enter into a full view
of listed posts and comment on them and like them if registered
and logged in"""

from django.shortcuts import render, get_object_or_404, reverse
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


class PostFullView(View):

    """ Sets the view for posts to be entered into in a new
    template under post_full_view and view approved comments
    and likes """

    def get(self, request, slug, *args, **kwargs):

        """ Displays the current post and approved comments.
        Sets the value for the like button to false and queries
        if the user has liked the post so that it can then be
        set to true for display"""

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_full_view.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        """ Sets the display and functionality to a user
        submitted comment calling on the comment form,
        checking its validity and saving to the database
        for apporval to then be displayed"""

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
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
                "liked": liked
            },
        )

    def delete_comment(self, request, id=id):

        """ Allows for comments to be deleted """

        comment = get_object_or_404(Comment, id=id)
        deletion = request.user(self, id=id)
        if (
            comment.name == deletion.username and deletion.is_authenticated
        ):
            comment.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                f'{"Your comment has been deleted"}',
            )
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class PostLike(View):

    """Sets the display and functionality of liking/Unliking posts"""

    def post(self, request, slug):

        """ Sets the parameters for a user to unlike a post.
        Checks if the user has already liked the post and if
        so, selecting like will unlike the post and vice versa.
        Upon liking or unliking the post will refresh and
        display the users current like status """

        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_full_view', args=[slug]))
