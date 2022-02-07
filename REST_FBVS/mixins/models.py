from unicodedata import category
from django.db import models

# Create your models here.


class ProductsModel(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(self):
        return self.id + self.name + self.unit + self.price