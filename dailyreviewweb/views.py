from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Prompt
from django.views import generic



class IndexView(generic.ListView):
    template_name = "dailyreviewweb/index.html"
    context_object_name = "all_prompts"
    def get_queryset(self):
        """Return all prompts"""
        return Prompt.objects.all()
