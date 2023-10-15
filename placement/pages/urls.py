from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("companies/", views.company, name="company"),
    path("login/", views.loginPage, name="Login"),
    path("logout/", views.logOut, name="Logout"),
    path("profile/", views.profile, name="Profile"),
    path("update-profile/", views.update_student_profile, name="Update-Profile"),
    path("education-update/", views.update_education, name="Update-Education"),
    path("loginauth",views.auth),
    path("students/", views.listStudent, name="Student"),
    path('details/<int:id>', views.student_profile, name='student_profile'),



]