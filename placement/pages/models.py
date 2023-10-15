from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
        
class Company(models.Model):
    logo = models.CharField(max_length=1500)
    CompanyName = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    details = models.TextField()
    MinGPA = models.FloatField()
    DeadLine = models.DateField()
    Departments = models.ManyToManyField(Department, related_name='eligible_companies')
    def __str__(self):
        return self.CompanyName

class Student(models.Model):
    #Basic Details
    gender = models.CharField(max_length=10,null=True)
    city = models.CharField(max_length=50, null=True)
    aadhar=models.CharField(max_length=50, null=True)
    gctmail = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    date_of_birth = models.DateField(null=True)
    
    #Education
    batch = models.IntegerField(null=True)
    rollnum=models.CharField(max_length=50, null=True)
    year = models.IntegerField(null=True)
    SSLC = models.FloatField(null=True)
    HSC = models.FloatField(null=True)
    isLatral = models.BooleanField(default=False)
    cgpa = models.FloatField(null=True)
    resume = models.CharField(max_length=200, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)


    # Others
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profileUrl = models.CharField(max_length=200,default="https://cdn-icons-png.flaticon.com/512/1999/1999625.png")
    bannerUrl = models.CharField(max_length=200,default="https://u-static.fotor.com/images/text-to-image/result/PRO-31d0bb5520b84354b1a2f395521b6a20.jpg")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
