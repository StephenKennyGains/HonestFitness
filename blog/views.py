""" Views allow for models to be displayed to the user and
are displayed by referencing them through the templates.
Below are the views to allow users to enter into a full view
of listed postsand comment on them and like them if registered
and logged in"""

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Review
from .forms import CommentForm, ReviewForm
from django.core.paginator import Paginator


class PostGeneral(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Pagination comes in at 3 posts to scroll earlier posts"""

    context_object_name = "category"
    template_name = "index.html"
    model = Post
    def get_queryset(self):
        myset = {
            "General": Post.objects.filter(status=1, category=1).order_by(
                "-created_on"),
            "Training": Post.objects.filter(status=1, category=2).order_by(
                "-created_on"),
            "Exercise": Post.objects.filter(status=1, category=3).order_by(
                "-created_on")
        }
        paginator = Paginator(Post, 3)
        return myset


class PostFullView(View):

    """ Sets the view for posts to be entered into in a new
    template under post_full_view and view approved comments
    and likes"""

    def get(self, request, slug, *args, **kwargs):

        """ Displays published posts, approved comments and likes """

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

        """ Sets the display and oredering of approved comments
        and checks for the log in status for display"""

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


class PostLike(View):

    """ Sets the display of liking/Unliking posts """

    def post(self, request, slug):

        """ Sets the parameters for a user to unlike a post
        if already liked and like if not already liked"""

        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_full_view', args=[slug]))


class Review(generic.ListView):

    """ Sets the view for posts to display to the homepage.
    Pagination comes in at 3 posts to scroll earlier posts"""

    model = Review
    queryset = Review.objects.filter(status=1).order_by(
        "-created_on")
    template_name = "reviews.html"
