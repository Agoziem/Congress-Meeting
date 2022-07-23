from django.db import models

class Programme(models.Model):
    name= models.CharField(max_length= 300, blank=True)
    Date= models.CharField(max_length= 300, blank=True)
    speaker= models.CharField(max_length= 300, blank=True)
    time= models.CharField(max_length= 300, blank=True)
    Venue= models.CharField(max_length= 300, blank=True)