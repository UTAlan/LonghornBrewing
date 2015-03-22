from django.db import models
from tinymce import models as tinymce_models

class HomePage(models.Model):
    title = models.CharField(max_length=200,blank=True)
    title_size = models.IntegerField(default=0)
    title_color = models.CharField(max_length=200,blank=True)
    title_font = models.CharField(max_length=200,blank=True)
    slogan = models.CharField(max_length=200,blank=True)
    slogan_size = models.IntegerField(default=0)
    slogan_color = models.CharField(max_length=200,blank=True)
    content_left = tinymce_models.HTMLField(blank=True)
    content_right = tinymce_models.HTMLField(blank=True)
    nav_color = models.CharField(max_length=200,blank=True)
    nav_hover_color = models.CharField(max_length=200,blank=True)
    slider_color = models.CharField(max_length=200,blank=True)
    slider_active_color = models.CharField(max_length=200,blank=True)
    border_color = models.CharField(max_length=200,blank=True)

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
