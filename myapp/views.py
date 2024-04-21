from django.shortcuts import render
from django.template import Template 
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello World!")

def home_page(request):
    return render(request, "index.html") 

def All_analytics(request):
    return render(request, "all-analytics.html") 

def Analytics(request):
    return render(request, "analytics.html")   

def try_file(request):
    return render(request, "try.html")  

def task_file(request):
    return render(request, "task.html")                
