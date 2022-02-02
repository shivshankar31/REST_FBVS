from tokenize import Name
from unicodedata import decimal
from django.db import models

# Create your models here.

class Students(models.Model):
    Id = models.IntegerField(primary_key=True, null=False)
    Name = models.CharField(max_length=50, null=False)
    Mark = models.DecimalField( max_digits=3, decimal_places=2)
    Location = models.CharField(max_length=50)

    def __str__(self):
        return self.Id + self.Name + self.Mark + self.location