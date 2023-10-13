from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("companies/", views.company, name="company"),
    path("login/", views.loginPage, name="Login"),


]