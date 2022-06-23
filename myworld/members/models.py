from django.db import models

# Create your models here.
class Members(models.Model):
    gruppe = models.ManyToManyField('gruppe', blank=True, related_name='items')
    name = models.CharField(max_length=255)
    modul = models.CharField(max_length=255)

class Gruppe(models.Model):
    name = models.CharField(max_length=255)