from django.db import models
from django.contrib.auth.models import User

from app.models import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' ' + self.products.title


    def total(self):
        return self.products.prix * 16 / 100

