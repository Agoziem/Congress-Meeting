from django.contrib import admin
from .models import *




# admin.site.register(data)
# admin.site.register(Subcription)
admin.site.register(Streaminglink)

@admin.register(data)
class DataAdmin(admin.ModelAdmin):
    list_display=('name','Occupation','date_registered')
    ordering=('name','date_registered')
    search_fields=('name','Zone','gender','Church','Occupation','School','level',)
    list_filter=('Occupation','level','Zone','gender',)

@admin.register(Subcription)
class SubAdmin(admin.ModelAdmin):
    search_fields=('email',)