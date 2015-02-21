from django.db import models

class SliderItem(models.Model):
    name = models.CharField(max_length=200,unique=True)
    active = models.BooleanField(default=True)
    image = models.ImageField()
    
    def __unicode__(self):
        return self.name
