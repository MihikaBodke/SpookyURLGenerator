from django.db import models

# Create your models here.
class Urls(models.Model):
    url = models.URLField()     
    customURL = models.CharField(max_length=100, unique=True)
    isShortened = models.BooleanField(default = "0", blank = True)



class SpookyThing(models.Model):
    thing = models.CharField(max_length=100)