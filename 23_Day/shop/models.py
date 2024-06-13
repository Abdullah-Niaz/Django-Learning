from django.db import models

# Create your models here.

class ShopForm(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    img = models.ImageField()

    # def __str__(self) -> str:
    #     return str(self.id)