from .models import UserReview
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ('user_title', 'user_location', 'user_reviewbody', 'user_rating')
