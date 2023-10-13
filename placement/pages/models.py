from django.db import models

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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    resume = models.FileField(upload_to='resumes/')
    education = models.TextField()
    skills = models.TextField()
    work_experience = models.TextField()
    references = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
