from django.shortcuts import render,redirect
from registration.models import *
from django.contrib import messages
from django.http import JsonResponse
import json

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
    data=json.loads(request.body)
    subemail=data['userdata']['email']
    sub_email=Subcription.objects.create(email=subemail)
    sub_email.save()
    return JsonResponse('submitted successfully',safe=False)
         
