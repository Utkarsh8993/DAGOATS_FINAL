from django.db import models

import datetime

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=1500)

    def __str__(self) :
        return f"{self.name} at {self.address}"
        
    




class Event(models.Model):
    name = models.CharField(max_length=500)
    venue = models.ForeignKey(Venue , on_delete = models.CASCADE , related_name="venue" )
    date = models.DateField(default= datetime.date.today())
    time = models.TimeField(default= datetime.datetime.now())
    duration = models.CharField(max_length=50)
    yop_choices = [
        ('First Year' , '1'),
        ('Second Year' , '2'),
        ('Third Year' , '3'),
        ('Fourth Year' , '4'),
    ]
    BRANCH_CHOICES =[
        ('Mechanical Engineering' , 'ME'),
        ('Computer Science Engineering','CSE'),
        ('Electronics and Communication Engineering','ECE'),
        ('Electrical Engineering','EE'),
        ('Engineering Physics','EPH' ),
        ('Civil Enginnering','CE'),
        ('Chemical Engineering', 'CHE'),
        ('Mathematics and Computing', 'MNC'),
        ('Metallurgy and Material sciences','META'),
        ('NON' , 'others or None of the Above')
    ]
    yop = models.CharField(choices=yop_choices, max_length=50)
    branch = models.CharField(choices=BRANCH_CHOICES , max_length=50,blank=True , null=True)
    description = models.CharField(max_length=10000)
    mobile = models.CharField(max_length=12 , blank=True , null=True)
    email = models.EmailField(blank=True, null=True)
    