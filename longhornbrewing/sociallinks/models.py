from django.db import models

class SocialLink(models.Model):
    name = models.CharField(max_length=200,blank=True)
    url = models.CharField(max_length=200,blank=True)
    image = models.ImageField()
    order = models.IntegerField(default=0)
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
