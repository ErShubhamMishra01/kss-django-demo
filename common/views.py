from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration

# def index(request):
#     return HttpResponse("Hi AKS")

def index(request):
    return render(request,'index.html')


def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def register(request):
    return render(request,'register.html')

def saveRegister(request):
    if request.method=="POST":
        name=request.POST.get('uname')
        gender=request.POST.get('ugender')
        email=request.POST.get('uemail')
        course=request.POST.get('ucourse')
        address=request.POST.get('uaddress')
        try:
            res=Registration(name=name,gender=gender,email=email,course=course,address=address)
            res.save()
            msg="Record saved successfully"
        except Exception as e:
            print(e)
            msg="Sorry, unable to save data please try again later."

    return render(request,'register.html',{'msg':msg})

