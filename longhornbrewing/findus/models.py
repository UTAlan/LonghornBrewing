from django.db import models
from tinymce import models as tinymce_models

class FindUs(models.Model):
    title = models.CharField(max_length=200,blank=True)
    slogan = models.CharField(max_length=200,blank=True)
    page_content = tinymce_models.HTMLField(blank=True)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Find Us"

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
