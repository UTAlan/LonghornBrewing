from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group

class ContactPage(models.Model):
    title = models.CharField(max_length=200,blank=True)
    title_size = models.IntegerField(default=0)
    business_hours_title = models.CharField(max_length=200,blank=True)
    business_hours = models.TextField(blank=True)
    tour_hours_title = models.CharField(max_length=200,blank=True)
    tour_hours = models.TextField(blank=True)
    address1 = models.CharField(max_length=200,blank=True)
    address2 = models.CharField(max_length=200,blank=True)
    phone = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200,blank=True)
    map_title = models.CharField(max_length=200,blank=True)
    map_image = models.ImageField()
    
    def __unicode__(self):
        return self.title