from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Prompt


def index(request):
    random_prompt = Prompt.objects.order_by("?").first()
    template = loader.get_template("polls/index.html")
    context = {"random_prompt": random_prompt}
    return HttpResponse(template.render(context, request))


def results(request, prompt_id):
    response = "You're looking at the results for prompt %s."
    return HttpResponse(response % prompt_id)
