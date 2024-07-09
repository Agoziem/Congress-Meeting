from django.urls import path
from .views import *

app_name = 'registration'
urlpatterns = [
    path('', register, name='register'),
    path('Submitregistrationform/',Submitregistrationform, name='Submit'),
    path('search/', search_users, name='search_users'),
    path('user-details/<int:user_id>/', user_details, name='user_details'),

]