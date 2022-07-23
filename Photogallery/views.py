from django.shortcuts import render
from .models import *

def gallery_view(request):
    category=year.objects.all()
    context={
        'year': category,
    }
    return render(request,'pictures.html',context)
