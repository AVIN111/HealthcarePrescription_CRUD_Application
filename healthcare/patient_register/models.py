from django.db import models
# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = (
        ('O', 'Others'),
        ('M', 'Male'),
        ('F', 'Female'),
    )

    DEPARTMENT_CHOICES = (
        ('ENT','ENT'),
        ('DERMATOLOGY','DERMATOLOGY'),
        ('NEUROLOGY','NEUROLOGY'),
        ('DENTAL','DENTAL')
    )

    PRECONDITIONS_CHOICES = (
        ('NONE','NONE'),
        ('ASTHMA','ASTHMA'),
        ('DIABETES','DIABETES'),
        ('HYPERTENSION','HYPERTENSION')
    )
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=100, blank=False, default='Unspecified', choices=GENDER_CHOICES)
    department = models.CharField(max_length=100, blank=False, default='Unspecified', choices=DEPARTMENT_CHOICES)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    precondition = models.CharField(max_length=100, blank=False, default='Unspecified', choices=PRECONDITIONS_CHOICES)
    allergic = models.BooleanField(default=False)
    height = models.FloatField(default=0)
    profile = models.ImageField(upload_to='images/',null=True,blank=True)
