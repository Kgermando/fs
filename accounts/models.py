from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField(upload_to = 'user-profile/',default='avatar.svg')
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=True)
    age = models.IntegerField(null=True)
    job = models.CharField(max_length = 100,null=True)
    bio = models.TextField(null=True)
    address = models.CharField(max_length = 100,null=True)
    contack_no = models.IntegerField(null=True)



