from django.db import models
from django.contrib.auth.models import User


class Prompt(models.Model):
    prompt_text = models.TextField("Text of Prompt")


class Entry(models.Model):
    entry_date = models.DateField("Date of Entry")
    entry_text = models.TextField("Text of Entry")
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
