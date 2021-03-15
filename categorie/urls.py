
from django.urls import path

from categorie.views import categorie


app_name = 'categorie'

urlpatterns = [
    path('', categorie, name="categorie"),
    path('<product_slug>/', categorie, name='categorie_slug'),
    # path('<motcle_slug>/', motcle_view, name='motcle_slug'),
    # path('<theme_slug>/', theme_view, name='theme_slug'),
]
 
