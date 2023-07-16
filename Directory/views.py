from django.shortcuts import render,redirect 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

def home_dir(request):
    context={

    }
    return render(request,'Directory/Homedir.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Directory:dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('Directory:login') #Redirect Calls on the Url function directory
    context={
        "form":form
    }
    return render(request,'accounts/register.html',context)

def logoutUser(request):
	logout(request)
	return redirect('Directory:directory')

# Main Profile Page
def profile(request):
    context={
        
    }
    return render(request,'profile/profile.html',context)



# Create Profile Page
def createprofile1(request):
    form1=bio()
    if request.method == 'POST':
        form1=bio(request.POST)
        if form1.is_valid():
                form1.save()
                form2=socialprofile()
                context={
                    "form":form2
                    }
                # user = form.cleaned_data.get('username')
                # messages.success(request, 'Account was created for ' + user)
                return render(request,'profile/create_profile2.html',context)
    context={
        "form":form1
    }
    return render(request,'profile/create_profile1.html',context)

def createprofile2(request):
    form2=socialprofile()
    if request.method == 'POST':
        form1=bio(request.POST)
        if form1.is_valid():
                form1.save()
                form3=Career()
                context={
                    "form":form3
                    }
                # user = form.cleaned_data.get('username')
                # messages.success(request, 'Account was created for ' + user)
                return render(request,'profile/create_profile3.html',context)
    context={
        "form":form1
    }
    return render(request,'profile/create_profile2.html',context)

def createprofile3(request):
    form1=Career()
    if request.method == 'POST':
        form1=bio(request.POST)
        if form1.is_valid():
                form1.save()
                # user = form.cleaned_data.get('username')
                # messages.success(request, 'Account was created for ' + user)
                return redirect('Directory:profile') #Redirect Calls on the Url function directory
    context={
        "form":form1
    }
    return render(request,'profile/profile3.html',context)


# edit/update Profile Page
def editprofile(request):
    context={
        
    }
    return render(request,'profile/edit_profile.html',context)

# delete Profile Page

def deleteprofile(request):
    context={
        
    }
    return render(request,'profile/delete_profile.html',context)

def dashboard_view(request):
    context={
    }
    return render(request,'Directory/main.html',context)


def Chart_view(request):
    context={
    }
    return render(request,'Directory/charts.html',context)

def Table_view(request):
    context={
    }
    return render(request,'Directory/Data-tables.html',context)

def Congress_view(request):
    context={
    }
    return render(request,'Directory/Congress.html',context)

def Worshipexperience_view(request):
    context={
    }
    return render(request,'Directory/Experience.html',context)

def ExamCampaign_view(request):
    context={
    }
    return render(request,'Directory/Campaign.html',context)


def Students_view(request):
    context={
    }
    return render(request,'Directory/students.html',context)

def Aluminai_view(request):
    context={
    }
    return render(request,'Directory/Seniorfriends.html',context)