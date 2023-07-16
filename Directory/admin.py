from django.contrib import admin
from .models import *

admin.site.register(bio)
admin.site.register(socialprofile)
admin.site.register(Career)


# @admin.register(bio)
# class DataAdmin(admin.ModelAdmin):
#     list_display=('id','name','Occupation','date_registered')
#     ordering=('name','date_registered')
#     search_fields=('id','name','Zone','gender','Church','Occupation','School','level',)
#     list_filter=('Occupation','level','Zone','gender',)

