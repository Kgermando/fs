
from django.urls import path

from cart.views import cart, delete_cart, add_to_cart

app_name = 'cart'

urlpatterns = [
    path('cart/<int:pk>/', cart, name='cart'),
    path('cart/<int:pk>/delete', delete_cart, name='delete_cart'),
    path('cart/add_to_cart/<int:pk>', add_to_cart, name='add_to_cart'),
]
