from django.db import models
from tinymce import models as tinymce_models

class Contact(models.Model):
    title = models.CharField(max_length=200,blank=True)
    title_size = models.IntegerField(default=0)
    title_color = models.CharField(max_length=200,blank=True)
    title_font = models.CharField(max_length=200,blank=True)
    slogan = models.CharField(max_length=200,blank=True)
    slogan_size = models.IntegerField(default=0)
    slogan_color = models.CharField(max_length=200,blank=True)
    content_color = models.CharField(max_length=200,blank=True)
    business_hours_title = models.CharField(max_length=200,blank=True)
    business_hours = tinymce_models.HTMLField(blank=True)
    tour_hours_title = models.CharField(max_length=200,blank=True)
    tour_hours = tinymce_models.HTMLField(blank=True)
    address1 = models.CharField(max_length=200,blank=True)
    address2 = models.CharField(max_length=200,blank=True)
    phone = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200,blank=True)
    map_title = models.CharField(max_length=200,blank=True)
    map_image = models.ImageField(blank=True)

    def __unicode__(self):
        return self.title
