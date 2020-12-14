from django.forms import ModelForm

from teamsoft.models import Feedback


class FeedBackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude=[]
        #fields = ("name", "email", "message")
