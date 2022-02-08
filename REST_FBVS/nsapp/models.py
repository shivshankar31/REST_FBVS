from django.db import models

# Create your models here.
class Author(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)

    def __str__(self):
        return self.FirstName + self.LastName

class Book(models.Model):
    title = models.CharField(max_length=50)
    Rating = models.CharField(max_length=50)
    Author = models.ForeignKey(Author, related_name = 'book', on_delete=models.CASCADE)

    def __str__(self):
        return self.title + self.Rating + self.Author