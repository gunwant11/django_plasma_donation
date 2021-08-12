from django.db import models

DONATE_CENTER=(
    ('1','Donation center 1'),
    ('2','Donation center 2'),
    ('3','Donation center 3')
)

GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
BLOOD_GROUP = (
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-')
    )

# Create your models here.
class DonorsInfo(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    age = models.IntegerField( blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=12,default=None)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP, null=True, default=None)
    weight = models.IntegerField(blank=True,null=True)
    negative_tested_on = models.DateField(auto_now=False, auto_now_add=False,null=True)
    city = models.CharField(max_length=200, null=True)
    donate_center = models.CharField(choices=DONATE_CENTER,max_length=12,default=None)
 
    def __str__(self):
        return self.name



