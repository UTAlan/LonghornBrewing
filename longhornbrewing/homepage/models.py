from django.db import models
from tinymce import models as tinymce_models

class HomePage(models.Model):
    title = models.CharField(max_length=200,blank=True)
    title_size = models.IntegerField(default=0)
    slogan = models.CharField(max_length=200,blank=True)
    slogan_size = models.IntegerField(default=0)
    content_left = tinymce_models.HTMLField(blank=True)
    content_right = tinymce_models.HTMLField(blank=True)
    
    def __unicode__(self):
        return self.title

class SliderItem(models.Model):
    name = models.CharField(max_length=200,unique=True)
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    link = models.CharField(max_length=200,blank=True)
    image = models.ImageField()
    
    def __unicode__(self):
        return self.name
