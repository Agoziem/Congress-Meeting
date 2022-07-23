from django.shortcuts import render
from .models import *
from django.contrib import messages

def register(request):
    if request.method=='POST':
        Name=request.POST.get('Name')
        Gender=request.POST.get('inlineRadioOptions')
        Address=request.POST.get('address')
        Contact=request.POST.get('Phonenumber')
        Email=request.POST.get('Emailaddress')
        status=request.POST.get('status')
        Church=request.POST.get('church')
        Zone=request.POST.get('zone')
        School=request.POST.get('School')
        Level=request.POST.get('level')
        
        data.objects.create(
			name=Name,
			gender=Gender,
			address=Address,
			Phonenumber=Contact,
			Emailaddress=Email,
			Occupation=status,
			School=School,
			Church=Church,
			Zone=Zone,
			level=Level,

        )
        
        try:
            mydata=data.objects.get(name=Name)
            Registered=True
            context={
                'id': mydata,
                'registered':Registered,     
            }
            messages.success(request,'You have Successfully registered for Students Congress 2022')
            return render(request,'register.html',context)
        except:
            # mydata=data.objects.get(name=Name)
            # mydata.delete()
            Registered=False
            context={
                'registered':Registered,
                
            }
            messages.error(request,'You have already Submitted, multiple instances cannot be recorded')
            return render(request,'register.html',context)
    context={
        
    }
    return render(request,'register.html',context)


