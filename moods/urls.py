from django.urls import path, include
from moods.views import home,create_mood
urlpatterns=[
path('',home),
path('create_mood/',create_mood),
]