from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Post

# Create your tests here.


class PostModelTestCase(TestCase):

    """ A test case to test use through model tests """

    def setup(self):
        """ Setup for model Testing """
        self.username='Jane'
        self.password='Pass12345'
        user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.content = Post.objects.create(
            content="Content Test"
        )
        self.client.login(username='Jane', password='Pass12345')
        self.post = Post.objects.create(
            title="Test Post",
            content=self.content,
            description="Test description",
            author=self.user,
        )

    def test_create_post(self):
        testpost = get_object_or_404(Post, title="Test Post")
        self.assertEqual(self.post.content, testpost.content)
