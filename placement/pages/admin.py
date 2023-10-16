from django.contrib import admin
from .models import Department, Company, Student, Application

admin.site.register(Department)
admin.site.register(Company)
admin.site.register(Student)
admin.site.register(Application)