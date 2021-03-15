
from django.urls import path

from projets.views import projets

app_name = 'projets'

urlpatterns = [
    path('', projets, name='projets'),
]
