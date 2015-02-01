from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group
from tinymce import models as tinymce_models

class HomePage(models.Model):
    title = models.CharField(max_length=200,blank=True)
    slogan = models.CharField(max_length=200,blank=True)
    content = tinymce_models.HTMLField(blank=True)
    
    def __unicode__(self):
        return self.title