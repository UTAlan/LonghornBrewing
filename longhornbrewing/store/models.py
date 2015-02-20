from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group

class Product(models.Model):
    name = models.CharField(max_length=200,blank=True,unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    display_sizes = models.BooleanField(default=False)
    image = models.ImageField()
    
    def __unicode__(self):
        return self.name

class Store(models.Model):
    title = models.CharField(max_length=200,blank=True)
    title_size = models.IntegerField(default=0)
    slogan = models.CharField(max_length=200,blank=True)
    slogan_size = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title