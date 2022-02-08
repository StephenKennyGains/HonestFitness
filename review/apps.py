"""Used to apply and configure the current
app to the project"""

from django.apps import AppConfig


class ReviewConfig(AppConfig):
    """Sets review app as the name to be used in the Appconfig"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review'
