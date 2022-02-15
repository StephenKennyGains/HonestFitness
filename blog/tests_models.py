from django.test import TestCase
from .models import Post

# Create your tests here.


class TestPostModel(TestCase):

    """ A test case to test use through model tests """

    def test_create_new_post(self):
        """ A test case to test use through model tests """
        item = Post.objects.create(title='General 1')
        self.assertFalse(item=done)
