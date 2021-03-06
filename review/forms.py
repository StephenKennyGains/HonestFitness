"""Imports forms from django and comment from models.
Used to render and post the form in post full view"""

from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Sets the Review Form to be used and pulls
    from forms.ModelForm"""

    class Meta:
        """ Sets the model as Review and relevant fields"""

        model = Review
        fields = ('title', 'location', 'reviewbody', 'rating')
