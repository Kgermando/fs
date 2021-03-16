from django.contrib import admin

from cart.models import Cart

admin.site.site_header = 'FASTSMART'
admin.site.site_title = "Interface d'administration"
# Register your models here.

admin.site.register(Cart)
