from django.http import HttpResponse
from django.shortcuts import render

def webpage1(request):
    return render(request, 'Lesson 1.html')