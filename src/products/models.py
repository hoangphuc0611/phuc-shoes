from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='static/products')
    color = models.CharField(max_length=100,default='#e1e7ed')

    def __str__(self):
        return self.name

class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.variant_name

   
