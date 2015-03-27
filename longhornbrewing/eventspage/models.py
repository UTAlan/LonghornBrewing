from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200,blank=True)
    slogan = models.CharField(max_length=200,blank=True)

    def __unicode__(self):
        return self.title
