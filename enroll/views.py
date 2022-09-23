from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def studentinfo(request):
    stud=Student.objects.get(pk=1)
    print('Myoutput',stud)
    return render(request,'enroll/studetails.html',{'stu':stud})