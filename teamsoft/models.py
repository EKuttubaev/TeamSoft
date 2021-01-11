from django import forms
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="")
    email = models.EmailField(verbose_name="", null=True, blank=True)
    message = models.CharField(max_length=255, verbose_name="")

    def __str__(self):
        return self.name
