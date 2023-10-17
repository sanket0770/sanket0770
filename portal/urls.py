import imp
from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login", views.loginuser, name="login"),
    path("signup", views.signup, name="signup"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('addtenant', views.addtenant, name='addtenant'),
    path('details', views.details, name="details"),
    path('message', views.mmessage, name="message"),
    path('msgshow', views.msgshow, name="msgshow"),

    path('show', views.show, name="show"),
    path('pdetails', views.pdetails, name="pdetails"),
    path('s_pdetails', views.s_pdetails, name="s_pdetails"),  
    path('logout', views.logoutuser , name="s_pdetails")  

]
