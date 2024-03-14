from django.db import models

# Create your models here.


class Product(models.Model): 
    id = models.AutoField(primary_key=True) 
    title=models.CharField(max_length=120) 
    conttne=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=15,decimal_places=2)
    
    