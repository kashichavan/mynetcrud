from django.shortcuts import render

# Create your views here.

def home(request):
    v="this is home page"
    return render(request,'home.html',context={'data':v})

def create(request):
    data="this is create view"
    return render(request,'create.html',{'data':data})
