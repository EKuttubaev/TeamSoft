from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    message = models.CharField(max_length=255, verbose_name="Текст")

    def __str__(self):
        return self.name
