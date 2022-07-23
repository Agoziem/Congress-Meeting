from django.urls import path
from .views import register

app_name = 'registration'
urlpatterns = [
    path('', register, name='register')
]