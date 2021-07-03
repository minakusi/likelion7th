from django.db import models

# Create your models here.
class Dongbang(models.Model):
    message = models.CharField(max_length=200)
    writer = models.CharField(max_length=20)
    date = models.DateField()