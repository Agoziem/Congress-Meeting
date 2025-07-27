from django.shortcuts import render,redirect
from registration.models import *
from Event.models import *
from django.contrib import messages
from django.http import JsonResponse
from Photogallery.models import gallery
import json

def home_view(request):
    link=Streaminglink.objects.all()
    programme=Programme.objects.all().order_by("-updated_at").first()
    programmeevents = ProgrammeEvent.objects.filter(programme=programme)
    speakers=Speaker.objects.filter(programme=programme)
    coordinator=Coordinator.objects.filter(programme=programme).first()
    images=gallery.objects.all()[:6]

    context={
        'link': link,
        'programme': programme,
        'programmeevents': programmeevents,
        'speakers': speakers,
        'coordinator': coordinator,
        'images': images,
    }
    return render(request,'home.html',context)

def data_view(request):
    allData=data.objects.all()
    context={
        'allData': allData,
    }
    return render(request,'data.html',context)



def subscription(request):
    data=json.loads(request.body)
    subemail=data['userdata']['email']
    sub_email=Subcription.objects.create(email=subemail)
    sub_email.save()
    return JsonResponse('submitted successfully',safe=False)
         
