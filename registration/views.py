from django.shortcuts import render
from .models import *
from Event.models import *
from django.contrib import messages
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404

def register(request):    
    zones=Zone.objects.all()
    levels=Level.objects.all()
    Occupation=Status.objects.all()
    programme = Programme.objects.all().order_by("updated_at").first()
    context={
        'zones':zones,
        'levels':levels,
        'Occupation':Occupation,
        'programme':programme
    }
    return render(request,'register.html',context)

# -----------------------------------------
# Submit registration form
# -----------------------------------------
from django.http import JsonResponse
import json

def Submitregistrationform(request,programme_id):
    programme = Programme.objects.get(id=programme_id)
    subdata = json.loads(request.body)
    name = subdata['name']
    gender = subdata['gender']
    Phonenumber = subdata['Phonenumber']
    Emailaddress = subdata['Emailaddress']
    address = subdata['address']
    church = subdata['church']
    zone = subdata['zone']
    status = subdata['status']
    School = subdata['School']
    level = subdata['level']

    registereddata, created = data.objects.get_or_create(name=name,programme=programme)
    registereddata.gender = gender
    registereddata.address = address
    registereddata.Phonenumber = Phonenumber
    registereddata.Emailaddress = Emailaddress
    registereddata.Occupation = status
    registereddata.School = School
    registereddata.Church = church
    registereddata.Zone = zone
    registereddata.level = level
    registereddata.save()

    print(registereddata)
    return JsonResponse('submitted successfully', safe=False)


def search_users(request):
    if request.method == 'GET' and 'name' in request.GET:
        search_name = request.GET.get('name')
        # Perform a case-insensitive search for names containing the search query
        results = data.objects.filter(name__icontains=search_name).values('id', 'name')
        return JsonResponse(list(results), safe=False)
    return JsonResponse([], safe=False)

def user_details(request, user_id):
    user = get_object_or_404(data, id=user_id)
    userdata = {
        'name': user.name,
        'gender': user.gender,
        'address': user.address,
        'church': user.Church,
        'phonenumber': user.Phonenumber,
        'emailaddress': user.Emailaddress,
        'zone': user.Zone,
        'occupation': user.Occupation,
        'school': user.School,
        'level': user.level
        # Add more fields as necessary
    }
    return JsonResponse(userdata)