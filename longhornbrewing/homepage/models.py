from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group
from tinymce import models as tinymce_models

class HomePage(models.Model):
    title = models.CharField(max_length=200,blank=True)
    title_size = models.IntegerField()
    slogan = models.CharField(max_length=200,blank=True)
    slogan_size = models.IntegerField()
    content_left = tinymce_models.HTMLField(blank=True)
    content_right = tinymce_models.HTMLField(blank=True)
    
    def __unicode__(self):
        return self.title