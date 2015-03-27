from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200,blank=True,unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    display_sizes = models.BooleanField(default=False)
    image = models.ImageField()

    def __unicode__(self):
        return self.name

class Store(models.Model):
    title = models.CharField(max_length=200,blank=True)
    slogan = models.CharField(max_length=200,blank=True)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
