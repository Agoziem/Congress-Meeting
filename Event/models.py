from django.db import models

class Programme(models.Model):
    name= models.CharField(max_length= 300, blank=True)
    description= models.TextField(blank=True)
    flier = models.ImageField(upload_to='fliers/', blank=True)
    date = models.CharField(max_length= 300, blank=True)
    theme = models.CharField(max_length= 300, blank=True)
    year = models.CharField(max_length= 300, blank=True)    
    venue = models.CharField(max_length= 300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.theme

    class Meta:
        ordering = ['updated_at']
    
class ProgrammeEvent(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    DAY_CHOICES = [
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    time = models.CharField(max_length=10,blank=True, null=True )
    description = models.TextField()

    def __str__(self):
        return f"{self.day} at {self.time}"
    
class Speaker(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='speakers/', blank=True)
    
    def __str__(self):
        return self.name
    

class Coordinator(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to='coordinators/', blank=True)
    
    def __str__(self):
        return self.name
