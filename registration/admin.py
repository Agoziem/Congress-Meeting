from django.contrib import admin
from .models import *


# class dataAdmin(admin.ModelAdmin):
#     list_display = ('gender',)

admin.site.register(data)
admin.site.register(Subcription)
admin.site.register(Streaminglink)


