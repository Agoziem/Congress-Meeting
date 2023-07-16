from django.urls import path
from .views import *

app_name = 'registration'
urlpatterns = [
    path('', register, name='register'),
    path('Submitregistrationform/',Submitregistrationform, name='Submit')
]