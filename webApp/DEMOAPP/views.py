from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request) :
    return render(request, 'DEMOAPP/hi.html'),
    return render(request, 'DEMOAPP/Lesson 1.html')
