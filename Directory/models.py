from django.db import models
from django.contrib.auth.models import User
GENDERCHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
STATUSCHOICES = (
    ('Student', 'Student'),
    ('Business', 'Business'),
    ('Enterprenuer', 'Enterprenuer'),
    ('Civil Servant', 'Civil Servant'),
    ('Politician', 'Politician'),
    ('Private Worker', 'Private Worker'),




)
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
    ('Youth Corp', 'Youth Corp'),
    ('Masters Student', 'Masters Student'),
    ('Phd Student', 'Phd Student'),

    


)

ZONECHOICE=(
    ('Awada', 'Awada'),
    ('Ugwuagba', 'Ugwuagba'),
    ('Holy Trinity', 'HolyTrinity'),
    ('Good Shepherd', 'Good Shepherd'),
    ('None', 'None'),

)

MARITALSTATUS=(
    ('Single', 'Single'),
    ('Married', 'Married'),
)


# Use the User Model for it , because the person must Sign-up before then
"""
"""




class bio(models.Model):
    user=models.OneToOneField(User,null=True , on_delete=models.CASCADE) #Models.cascade simply means when a User is deleted, delete its relationship to the Profile Models
    profilepicture=models.ImageField(upload_to='assets', blank=True)
    FirstName=models.CharField(max_length= 300, blank=True)
    MiddleName=models.CharField(max_length= 300, blank=True)
    LastName=models.CharField(max_length= 300, blank=True)
    gender= models.CharField(max_length= 300, blank=True, choices=GENDERCHOICES)
    Day_of_Birth= models.IntegerField(blank=False)
    Month_of_Birth= models.CharField(max_length= 300, blank=True)
    Phonenumber= models.CharField(max_length= 300, blank=True)
    marital_Status= models.CharField(max_length= 300, blank=True, choices=MARITALSTATUS)
    Name_of_spouse= models.CharField(max_length= 300, blank=True)
    Residential_address= models.CharField(max_length= 300, blank=True)
    Residential_LGA=models.CharField(max_length= 300, blank=True)
    Residential_State=models.CharField(max_length= 300, blank=True)
    Home_town=models.CharField(max_length= 300, blank=True)
    LGA=models.CharField(max_length= 300, blank=True)
    State=models.CharField(max_length= 300, blank=True)
    Hobbies=models.CharField(max_length= 300, blank=True)
    Church = models.CharField(max_length= 300, blank=True)
    Zone = models.CharField(max_length= 300, blank=True ,choices=ZONECHOICE)
    Branch = models.CharField(max_length= 300, blank=True)
    date_registered=models.DateTimeField(auto_now_add=True)
    

class socialprofile(models.Model):
    user=models.OneToOneField(User,null=True , on_delete=models.CASCADE)
    email=models.EmailField(max_length= 300, blank=True)
    Whatsapp=models.CharField(max_length= 300, blank=True)
    twitter=models.CharField(max_length= 300, blank=True)
    instagram=models.CharField(max_length= 300, blank=True)
    linkedin=models.CharField(max_length= 300, blank=True)
    facebook=models.CharField(max_length= 300, blank=True)
    date_registered=models.DateTimeField(auto_now_add=True)

class Career(models.Model):
    user=models.OneToOneField(User,null=True , on_delete=models.CASCADE)
    Occupation = models.CharField(max_length= 300, blank=True, choices=STATUSCHOICES)
    profession=models.CharField(max_length= 300, blank=True)
    current_location_Business=models.CharField(max_length= 300, blank=True)
    Name_of_organization=models.CharField(max_length= 300, blank=True)
    Name_of_Business=models.CharField(max_length= 300, blank=True)
    School= models.CharField(max_length= 300, blank=True)
    level= models.CharField(max_length= 300, blank=True , choices=LEVELCHOICES)
    date_registered=models.DateTimeField(auto_now_add=True)

    
    
    


