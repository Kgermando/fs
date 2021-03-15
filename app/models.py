from django.db import models
from django.db.models.signals import pre_save
from tinymce import HTMLField

from fastsmart.utils import unique_slug_generator
from categorie.models import (Category, MotCles, Theme)

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=50, db_index=True)
    slug        = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    img         = models.ImageField(upload_to='produit_img/')
    img2        = models.ImageField(upload_to='produit_img/')
    img3        = models.ImageField(upload_to='produit_img/')
    img4        = models.ImageField(upload_to='produit_img/')
    resume      = models.CharField(max_length=100)
    description = HTMLField('description')
    prix        = models.IntegerField()
    # quantity    = models.IntegerField(default=1, null=True)
    rate        = models.IntegerField(null=True, blank=True)
    preference  = models.BooleanField(default=False, null=True, help_text='Favoris')
    promotion   = models.IntegerField(null=True, help_text='Pourcentage de la promotion')
    promos      = models.BooleanField(default=False, null=True)
    categorie   = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    Mot_cles    = models.ForeignKey(MotCles, on_delete=models.CASCADE, null=True, blank=True)
    themes      = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True, blank=True)
    url_test    = models.CharField(max_length=100, null=True, blank=True)
    page_views  = models.IntegerField(default=0) # nombre des vues par page
    created     = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse("app:search-view", kwargs={"id": self.id})

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('app:search-view', args=[self.id, self.slug])

    def promotions(self):
        return self.prix * self.promotion / 100

    class Meta:
        db_table = 'product'
        ordering = ('title',)
        index_together = (('id', 'slug'),)


class ContactForm(models.Model):
    name    = models.CharField(max_length=50)
    email   = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Product)
