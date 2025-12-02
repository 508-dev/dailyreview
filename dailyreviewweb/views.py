from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Prompt
from django.views import generic



class IndexView(generic.ListView):
    template_name = "dailyreviewweb/index.html"

    def get_queryset(self):
        """Return all prompts"""
        return Prompt.objects.all()


def results(request, prompt_id):
    response = "You're looking at the results for prompt %s."
    return HttpResponse(response % prompt_id)
