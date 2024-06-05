from django.contrib import admin

from .models import *
# Register your models here


class EcommerceProductAdmin(admin.ModelAdmin):
    list_display = ("product_name",
                    "product_price",
                    "description",
                    "category",
                    "brand",
                    "image",
                    "stock_quantity",
                    "created_at",
                    "updated_at", 
                    "is_featured", 
                    "is_available")


admin.site.register(EcommerceProduct,EcommerceProductAdmin)
