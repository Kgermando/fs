from django.contrib import admin

from app.models import Product, ContactForm, Like

admin.site.site_header = 'FASTSMART'
admin.site.site_title = "Interface d'administration"
# Register your models here.


admin.site.register(Product)
admin.site.register(ContactForm)
admin.site.register(Like)
