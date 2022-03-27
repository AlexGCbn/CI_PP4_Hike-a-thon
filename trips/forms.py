from .models import Review, Request
from django import forms


class ReviewForm(forms.ModelForm):
    """
    User Review form
    """
    class Meta:
        model = Review
        fields = ('comment', 'rating', )


class RequestForm(forms.ModelForm):
    """
    Trip Request form
    """
    class Meta:
        model = Request
        fields = ('destination', 'description')
