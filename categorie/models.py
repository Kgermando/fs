from django.db import models
from django.db.models.signals import pre_save

from fastsmart.utils import unique_slug_generator_categorie

from fastsmart.constant import CATEGORIES, CATEGORIES_THEME, CATEGORIES_MOT_CLE

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=8, choices=CATEGORIES)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('categorie:categorie_slug', args=[self.slug])


class MotCles(models.Model):
    name = models.CharField(max_length=18, choices=CATEGORIES_MOT_CLE)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('categorie:motcle_slug', args=[self.slug])


class Theme(models.Model):
    name = models.CharField(max_length=8, choices=CATEGORIES_THEME)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('categorie:theme_slug', args=[self.slug])


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_categorie(instance)


pre_save.connect(tag_pre_save_receiver, sender=Category)
pre_save.connect(tag_pre_save_receiver, sender=MotCles)
pre_save.connect(tag_pre_save_receiver, sender=Theme)
