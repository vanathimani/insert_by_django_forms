from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}

    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():

            Sname=SFDO.cleaned_data['Sname']
            Sid=SFDO.cleaned_data['Sid']
            Semail=SFDO.cleaned_data['Semail']

            So=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            So.save()

            return HttpResponse('data inserted')

            

        else:

            return HttpResponse("invaild data")



    return render(request,'insert_student.html',d)