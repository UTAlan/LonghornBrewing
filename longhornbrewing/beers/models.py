from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group

class Beer(models.Model):
    name = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField()
    
    def __unicode__(self):
        return self.name

class OurBeer(models.Model):
    title = models.CharField(max_length=200,blank=True)
    title_size = models.IntegerField(default=0)
    slogan = models.CharField(max_length=200,blank=True)
    slogan_size = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title