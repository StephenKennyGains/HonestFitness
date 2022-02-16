from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    """ view tests """
    def test_get_index(self):
        """ Get home page tests """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
