from django.contrib import admin

from .models import Prompt, Entry

admin.site.register(Prompt)
admin.site.register(Entry)
