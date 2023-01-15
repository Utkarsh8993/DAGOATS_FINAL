from django.db import models
from elections.models import Candidate
# Create your models here.
from .manager import UserManager
from django.contrib.auth.models import AbstractUser
from events.models import Event


class User(AbstractUser):
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
    YEAR_CHOICES = [
        ('First' , '1'),
        ('Second' , '2'),
        ('Third' , '3'),
        ('Fourth' , '4'),
    ]
    username = None
    branch = models.CharField(max_length=50,null=True , blank=True , choices=BRANCH_CHOICES)
    name  = models.CharField(max_length=32)
    enrolno = models.CharField(max_length=8  , blank=True)
    email = models.EmailField(unique = True, )
    year = models.CharField(max_length=50,null=True , blank=True , choices=YEAR_CHOICES)
    events=models.ManyToManyField(Event, blank=True, related_name="user")
    organised_events=models.ManyToManyField(Event, blank=True, related_name="manager")
    vote1=models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="voter12", null=True,blank=True)
    vote2=models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="voter23", null=True,blank=True)
    vote3=models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="voter31", null=True,blank=True)

    vote_1_bool = models.BooleanField(default=False)
    vote_2_bool = models.BooleanField(default=False)
    vote_3_bool = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return f"{self.email}"



