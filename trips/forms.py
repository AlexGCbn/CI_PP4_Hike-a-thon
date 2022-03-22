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

    def clean_destination(self):
        destination = self.cleaned_data['destination']
        if Request.objects.filter(destination=destination).exists():
            raise forms.ValidationError('Destination already requested')
        return destination
