from django import forms
from django.forms import ModelForm

from teamsoft.models import Feedback


class FeedBackForm(ModelForm):

    class Meta:
        model = Feedback
        exclude = []
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Full Name'}),
            "email": forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            "message": forms.Textarea(attrs={'placeholder': 'Message'})

        }
