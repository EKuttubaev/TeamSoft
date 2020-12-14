from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from teamsoft.forms import FeedBackForm
from teamsoft.models import Feedback


class IndexView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        return render(request, "index.html", context={
            "header": "Main page"
        })


class FeedbackHandler(TemplateView):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        form = FeedBackForm()

        if request.method == "POST":
            form = FeedBackForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")

        return render(request, self.template_name, {"form": form})


class NewFormTest(TemplateView):
    template_name = "newformtest.html"

    def dispatch(self, request, *args, **kwargs):
        form = FeedBackForm()

        if request.method == "POST":
            form = FeedBackForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")

        return render(request, self.template_name, {"form": form})
