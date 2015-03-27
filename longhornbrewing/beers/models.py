from django.db import models
from tinymce import models as tinymce_models

class Beer(models.Model):
    name = models.CharField(max_length=200,blank=True)
    name_size = models.IntegerField(default=0)
    name_color = models.CharField(max_length=200,blank=True)
    description = tinymce_models.HTMLField(blank=True)
    image = models.ImageField()

    def __unicode__(self):
        return self.name

class OurBeer(models.Model):
    title = models.CharField(max_length=200,blank=True)
    slogan = models.CharField(max_length=200,blank=True)

    def __unicode__(self):
        return self.title
