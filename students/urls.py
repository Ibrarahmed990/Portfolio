from django.contrib import admin
from django.urls import path
from students import views

 
urlpatterns = [  
    #path("", views.register, name ='example')
    path("", views.studentinfo, name ='students')
]