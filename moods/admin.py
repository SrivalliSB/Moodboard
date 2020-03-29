from django.contrib import admin
from moods.models import Mood, Action, Moodlog

admin.site.register([Mood, Action, Moodlog])
