from django.db import models
from tinymce import models as tinymce_models

class FindUs(models.Model):
    title = models.CharField(max_length=200,blank=True)
    title_size = models.IntegerField(default=0)
    title_color = models.CharField(max_length=200,blank=True)
    title_font = models.CharField(max_length=200,blank=True)
    slogan = models.CharField(max_length=200,blank=True)
    slogan_size = models.IntegerField(default=0)
    slogan_color = models.CharField(max_length=200,blank=True)
    page_content = tinymce_models.HTMLField(blank=True)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Find Us"
