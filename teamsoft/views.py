from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from teamsoft.forms import FeedBackForm
from teamsoft.models import Feedback
from teamsoft.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


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
                self.notify_about_new_message(request, form.instance)
                messages.success(request, "Ваше сообщение отправлено")
                return redirect("/")

        return render(request, self.template_name, {"form": form})

    def notify_about_new_message(self, request,feedback):
        message = f"Вам отправлено сообщение\n\n" \
                  f"{feedback.message} от {feedback.name}  с электронной почты {feedback.email}\n\n"
        send_mail("Отправлено сообщение", message, settings.DEFAULT_FROM_EMAIL, ["kuttubaev.erkin@gmail.com"], False)
