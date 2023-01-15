from django.db import models



# Create your models here.
class Candidate(models.Model):
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
    email = models.EmailField(null=True , blank=True)
    name = models.CharField(max_length=32)
    branch = models.CharField(choices=BRANCH_CHOICES , max_length=50)
    enrolno = models.CharField(max_length=8)
    votes = models.IntegerField(default=0)
    image=models.ImageField(null=True, blank=True, upload_to='images/')
    voted_for = models.BooleanField(default=False)
    bio = models.CharField(max_length=5000)
    year = models.CharField(max_length=50,null=True , blank=True , choices=YEAR_CHOICES)
    vote5 = models.IntegerField(default=0)
    vote3 = models.IntegerField(default=0)
    vote1 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.email}"

