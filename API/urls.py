from django.urls import path
from API import views
urlpatterns = [
    path('',views.index,name="index"),  
]