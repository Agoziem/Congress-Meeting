from django.urls import path
from .views import *
# this is a comment 
app_name = 'Directory'
urlpatterns = [
    path('', home_dir, name='directory'),
    path('login/', loginPage, name='login'),
    path('signup/', registerPage, name='sign-up'),
    path('logout/', logoutUser, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('Charts/', Chart_view, name='charts'),
    path('Tables/', Table_view, name='tables'),
    path('Congress/', Congress_view, name='Congress'),
    path('Worshipexperience/', Worshipexperience_view, name='Worshipexperience'),
    path('ExamCampaign/', ExamCampaign_view, name='ExamCampaign'),
    path('Students/', Students_view, name='Students'),
    path('Aluminai/', Aluminai_view, name='Aluminai'),
    path('profile/',profile,name='profile'),
    path('createprofile1/',createprofile1,name='bio'),
    path('createprofile2/',createprofile2,name='socialprofile'),
    path('createprofile3/',createprofile3,name='career')
]

