from django.shortcuts import render,redirect
from registration.models import *
from django.contrib import messages


def home_view(request):
    link=Streaminglink.objects.all()
    context={
        'link': link,
    }
    return render(request,'home.html',context)

# def index_view(request):  
    context={
        
    }
    return render(request,'index.html',context)


def subscription(request):
    Submitted=False
    if request.method=='POST':
         Sub=request.POST.get('sub')
         Subcription.objects.create(
            email=Sub
         )
         Submitted=True
         context={
            'submitted': Submitted,
         }
         
         return render(request,'home.html',context)
    context={
            'submitted': Submitted,
         }
    return render(request,'home.html',context)
         
