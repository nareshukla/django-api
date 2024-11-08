from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name

