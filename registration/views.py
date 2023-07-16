from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import JsonResponse
import json

def register(request):    
    # try:
    #     mydata=data.objects.get(name=Name)
    #     Registered=True
    #     context={
    #         'id': mydata,
    #         'registered':Registered,     
    #     }
    #     messages.success(request,'You have Successfully registered for Students Congress 2022')
    #     return render(request,'register.html',context)
    # except:
    #     # mydata=data.objects.get(name=Name)
    #     # mydata.delete()
    #     Registered=False
    #     context={
    #         'registered':Registered,
            
    #     }
    #     messages.error(request,'You have already Submitted, multiple instances cannot be recorded')
    context={

    }
    return render(request,'register.html',context)


def Submitregistrationform(request):
    subdata=json.loads(request.body)
    name=subdata['userdata']['name']
    gender=subdata['userdata']['gender']
    Phonenumber=subdata['userdata']['Phonenumber']
    Emailaddress=subdata['userdata']['Emailaddress']
    address=subdata['userdata']['address']
    church=subdata['userdata']['church']
    zone=subdata['userdata']['zone']
    status=subdata['userdata']['status']
    School=subdata['userdata']['School']
    level=subdata['userdata']['level']

    sub_data=data.objects.create(
			name=name,
			gender=gender,
			address=address,
			Phonenumber=Phonenumber,
			Emailaddress=Emailaddress,
			Occupation=status,
			School=School,
			Church=church,
			Zone=zone,
			level=level
        )
    sub_data.save()
    return JsonResponse('submitted successfully',safe=False)