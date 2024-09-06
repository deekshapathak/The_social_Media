from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "placeholder": "Enter your tweet here",
            "class": "form-control",
        }),
        label=""
    )

    class Meta:
        model = Tweet
        exclude = ("user",)  # Add a comma to make this a tuple
