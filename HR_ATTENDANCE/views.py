from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hr_atend_home(request):
    return render(request , "HR_ATTENDANCE/home.html")
