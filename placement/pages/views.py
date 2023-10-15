from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        return render(request,'index.html',{"user":student,"tab":"home"})
    else:
        return render(request,'index.html',{"user":None,"tab":"home"})
        

def loginPage(request):
    return render(request,'login.html')
@login_required
def company(request):
    companies = Company.objects.all()
    student = Student.objects.get(user=request.user)
    return render(request,'company.html',{"companies":companies,"user":student,"tab":"company"})
    

def auth(request):
    if request.method == 'POST':
        form_data = request.POST
        username = form_data.get('username')
        password = form_data.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.info(request, "You are now logged in.")
            return redirect('/')  # Redirect to your desired URL
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html')

def logOut(request):
    logout(request)
    messages.info(request, "You are now logged out.")
    return redirect('/')

@login_required
def profile(request):
    student = Student.objects.get(user=request.user)
    date_of_birth = student.date_of_birth
    formatted_date = date_of_birth.strftime('%Y-%m-%d')
    return render(request,'profile.html',{"user":student,"tab":"profile","dob":formatted_date})

def update_student_profile(request):
    print("Hello")
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        # Retrieve other fields similarly

        # Update the student's profile
        student = request.user.student  # Assuming you have a user-student relationship
        student.first_name = first_name
        student.last_name = last_name
        student.email = email
        student.phone_number = phone_number
        student.address = address
        student.date_of_birth = dob
        # Update other fields similarly

        student.save()

        return JsonResponse({'message': 'Student profile updated successfully'})

def update_education(request):
    if request.method == 'POST':
        # Retrieve form data
        batch = request.POST.get('batch')
        rollnum = request.POST.get('rollnum')
        year = request.POST.get('year')
        SSLC = request.POST.get('SSLC')
        HSC = request.POST.get('HSC')
        cgpa = request.POST.get('cgpa')
        resume = request.POST.get('resume')

        # Update the student's education information
        student = request.user.student  # Assuming you have a user-student relationship
        student.batch = batch
        student.rollnum = rollnum
        student.year = year
        student.SSLC = SSLC
        student.HSC = HSC
        student.cgpa = cgpa
        student.resume = resume

        student.save()

        return JsonResponse({'message': 'Education information updated successfully'})


def listStudent(request):
    students = Student.objects.all()
    return render(request,'students.html',{"students":students,"tab":"student"})

def student_profile(request, id):
    student = Student.objects.get(id=id)
    date_of_birth = student.date_of_birth
    formatted_date = date_of_birth.strftime('%Y-%m-%d')
    print(formatted_date)
    return render(request,'OtherProfile.html',{"user":student,"tab":"profile","dob":formatted_date})

