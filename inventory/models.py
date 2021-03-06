from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):              #  on Python 2
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location,related_name='items')
    brand = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField()
    added_by = models.ForeignKey(User)
    added_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):              #  on Python 2
        return self.name
