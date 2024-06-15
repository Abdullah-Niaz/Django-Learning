from django.db import models

# Create your models here.


class ShopForm(models.Model):
    name = models.CharField(blank=True,max_length=20)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)