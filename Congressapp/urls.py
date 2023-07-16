
from django.contrib import admin
from django.urls import path,include
from .views import home_view,subscription
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,name='home'),
    # path('dashboard/',index_view, name='dashboard'),
    path('subscription/', subscription ,name='Subscription'),
    path('Photogallery/', include('Photogallery.urls')),
    path('registration/', include('registration.urls')),
    # path('Directory/', include('Directory.urls')),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header='ACM Awada Arch (Student Forum)'
admin.site.index_title='Site Administration'
