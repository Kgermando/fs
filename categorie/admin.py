from django.contrib import admin
from categorie.views import categorie

from categorie.models import Category, MotCles, Theme

admin.site.site_header = 'FASTSMART'
admin.site.site_title = "Interface d'administration"
# Register your models here.

admin.site.register(Category)
admin.site.register(MotCles)
admin.site.register(Theme)
