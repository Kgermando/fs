from django.contrib import admin
from categorie.views import categorie

from categorie.models import Category, MotCles, Theme
# Register your models here.

admin.site.register(Category)
admin.site.register(MotCles)
admin.site.register(Theme)
