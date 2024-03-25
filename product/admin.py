from django.contrib import admin

# Register your models here.

from .models import Product2,Category

admin.site.register(Product2)
admin.site.register(Category)

