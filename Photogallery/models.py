from pydoc_data.topics import topics
from unicodedata import category
from django.db import models

class year(models.Model):
    Year=models.CharField(max_length=100, blank=True)
    topic=models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.topic)

class gallery(models.Model):
    category=models.ForeignKey(year, related_name='cate' , on_delete=models.CASCADE , blank = True,null=True)
    Photo=models.ImageField(upload_to='assets')

    def __str__(self):
        return str(self.category)


