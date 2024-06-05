from django.db import models

# Create your models here.

from django.db import models

class EcommerceProduct(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    stock_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.product_name
