from django.shortcuts import render
from students.models import Student
# Create your views here.
def studentinfo(request):
    stud = Student.objects.all()
    print("Myoutput",stud)
    return render(request,'studetails.html',{'stu': stud})