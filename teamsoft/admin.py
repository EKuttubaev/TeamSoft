from django.contrib.admin import ModelAdmin, site

from teamsoft.models import Feedback


class TeamsoftAdmin(ModelAdmin):
    list_display = ["name","email","message"]

site.register(Feedback)