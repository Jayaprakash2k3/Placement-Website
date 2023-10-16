from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import csv
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

def company_profile(request, id):
    company = Company.objects.get(id=id)
    student = Student.objects.get(user=request.user)
    applications = Application.objects.filter(company=company)
    eli={"minCGPA":student.cgpa>=company.MinCGPA,"minSSLC":student.SSLC>=company.MinSSLC,"minHSC":student.HSC>=company.MinHSC,"dualPlace":((not student.isPlaced) or company.dualPlacement),"deadline":company.DeadLine>timezone.now()}
    applied = len(Application.objects.filter(student=student,company=company))!=0
    print(eli)
    return render(request,'companyProfile.html',{"company":company,"students":applications,"applied":applied,"eligible":eli})

def applicationLink(request,cid):
    student = Student.objects.get(user=request.user)
    company = Company.objects.get(id=cid)
    x=Application.objects.filter(student=student,company=company)
    if(x):
        return redirect('/company/'+str(cid))
    else:
        application = Application.objects.create(student=student, company=company)
        return redirect('/company/'+str(cid))

def withdraw(request,cid):
    student = Student.objects.get(user=request.user)
    company = Company.objects.get(id=cid)
    x=Application.objects.get(student=student,company=company)
    x.delete()
    return redirect('/company/'+str(cid))

def downloadPage(request,cid):
    student = Student.objects.get(user=request.user)
    company = Company.objects.get(id=cid)
    application = Application.objects.filter(company=company)
    if student.isPR:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="'+company.CompanyName+' DB.csv"'
            writer = csv.writer(response)
            x=0
            writer.writerow(['SlNo.',"Roll Number",'Name', 'First Name', 'Last Name','Gender','Department','GCT Mail','Personal Mail','Phone Number',"CGPA","SSLC","HSC","DOB","Address","City","Resume"])
            for row in application:
                writer.writerow([x,row.student.rollnum,row.student, row.student.first_name, row.student.last_name,row.student.gender,row.student.department,row.student.gctmail,row.student.email,row.student.phone_number,row.student.cgpa,row.student.SSLC,row.student.HSC,row.student.date_of_birth,row.student.address,row.student.city,row.student.resume])
                x+=1
            return response
        # return render(request,'download.html')
    else:
        return redirect('/company/'+str(cid))