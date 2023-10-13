from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def loginPage(request):
    return render(request,'login.html')
def company(request):
    companies = Company.objects.all()
    print(type(companies[0].DeadLine))
    return render(request,'company.html',{"companies":companies,"tab":"company"})
    # return render(request,'company.html',{"companyCount":5,"tab":"company"})