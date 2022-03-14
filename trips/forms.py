from .models import Review, Request
from django import forms


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('comment', 'rating', )


class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ('destination', 'description')
