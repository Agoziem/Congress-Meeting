from django.db import models
from Event.models import Programme

GENDERCHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


STATUSCHOICES = (
    ('Student', 'Student'),
    ('Youth Corp', 'Youth Corp'),
    ('Business', 'Business'),
    ('Enterprenuer', 'Enterprenuer'),
    ('Civil Servant', 'Civil Servant'),
    ('Politician', 'Politician'),
    ('Private Worker', 'Private Worker'),
)

class Status(models.Model):
    status= models.CharField(max_length= 300, blank=True, choices=STATUSCHOICES,unique=True)
    def __str__(self):
        return str(self.status)


LEVELCHOICES = (
    ('Primary', 'Primary'),
    ('Jss1', 'Jss1'),
    ('Jss2', 'Jss2'),
    ('Jss3', 'Jss3'),
    ('Ss1', 'Ss1'),
    ('Ss2', 'Ss2'),
    ('Ss3', 'Ss3'),
    ('Aspirant', 'Aspirant'),
    ('Jupeb', 'Jupeb'),
    ('Pre-Science/Pre-degree', 'Pre-Science/Pre-degree'),
    ('100l', '100l'),
    ('200l', '200l'),
    ('300l', '300l'),
    ('400l', '400l'),
    ('500l', '500l'),
    ('600l', '600l'),
    ('700l', '700l'),
    ('Graduate', 'Graduate'),
    ('Masters Student', 'Masters Student'),
    ('Phd Student', 'Phd Student'),
)


class Level(models.Model):
    level= models.CharField(max_length= 300, blank=True, choices=LEVELCHOICES,unique=True)
    def __str__(self):
        return str(self.level)

ZONECHOICE=(
    ('Awada', 'Awada'),
    ('Ugwuagba', 'Ugwuagba'),
    ('Holy Trinity', 'HolyTrinity'),
    ('Good Shepherd', 'Good Shepherd'),
    ('None', 'None'),
)

class Zone(models.Model):
    zone= models.CharField(max_length= 300, blank=True, choices=ZONECHOICE,unique=True)
    def __str__(self):
        return str(self.zone)

class data(models.Model):
    name= models.CharField(max_length= 300, blank=True)
    gender= models.CharField(max_length= 300, blank=True, choices=GENDERCHOICES)
    address= models.CharField(max_length= 300, blank=True)
    Church= models.CharField(max_length= 300, blank=True)
    Phonenumber= models.CharField(max_length= 300, blank=True)
    Emailaddress= models.CharField(max_length= 300, blank=True)
    Zone = models.CharField(max_length= 300, blank=True)
    Occupation= models.CharField(max_length= 300, blank=True)
    School= models.CharField(max_length= 300, blank=True)
    level= models.CharField(max_length= 300, blank=True)
    date_registered=models.DateTimeField(auto_now_add=True)
    Attended=models.BooleanField(default=False)
    programme=models.ForeignKey(Programme, on_delete=models.CASCADE, blank=True, null=True) 
    
    def __str__(self):
        return str(self.name)

class Streaminglink(models.Model):
    Mixlr=models.CharField(max_length= 300, blank=True)
    Telegram=models.CharField(max_length= 300, blank=True)

    def __str__(self):
        return str(self.Mixlr)




class Subcription(models.Model):
    email=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.email)
