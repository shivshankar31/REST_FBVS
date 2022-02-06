from django.db import models
from django.forms import IntegerField

# Create your models here.
class Employees(models.Model):
    Id = models.IntegerField(primary_key=True, null=False)
    Name = models.CharField(max_length=50, null=False)
    Salary = models.IntegerField(max_length=5, null=False)
    Department = models.CharField(max_length=50)

    def __str__(self):
        return self.Id + self.Name + self.Salary + self.Department