from django.contrib import admin
from .models import *

# admin.site.register(data)
# admin.site.register(Subcription)
admin.site.register(Streaminglink)

@admin.register(data)
class DataAdmin(admin.ModelAdmin):
    list_display=('id','name','Occupation','date_registered','Attended')
    ordering=('name','date_registered')
    search_fields=('id','name','Zone','gender','Church','Occupation','School','level',)
    list_filter=('Attended','Occupation','level','Zone','gender',"programme")

@admin.register(Subcription)
class SubAdmin(admin.ModelAdmin):
    search_fields=('email',)


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    search_fields=('zone',)
    list_display=('zone',)
    ordering=('zone',)
    list_filter=('zone',)

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    search_fields=('level',)
    list_display=('level',)
    ordering=('level',)
    list_filter=('level',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    search_fields=('status',)
    list_display=('status',)
    ordering=('status',)
    list_filter=('status',)