
from django.urls import path

from app.views import index, view, contact

app_name = 'app'

urlpatterns = [
    path('', index, name="home"),
    path('product/<slug:slug>/', view, name="view"),
    path('product/<int:id>/', view, name="search-view"),
    path('contact/', contact, name="contact"),
]
