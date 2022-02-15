from django.test import TestCase
from .forms import CommentForm

# Create your tests here.


class TestCommentForm(TestCase):

    """ Form Tests """

    def test_form_item_is_required(self):

        """ Test Comment Form required """

        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_set_in_meta(self):

        """ Test Comment Form required """

        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))
