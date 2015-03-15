from django.db import models

class Background(models.Model):
    name = models.CharField(max_length=200,blank=True)
    color_code = models.CharField(max_length=200,blank=True)

    def __unicode__(self):
        return self.name
