from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Dashboard',views.Dashboard,name='Dashboard'),
    path('Mylibrary',views.Mylibrary,name='Mylibrary'),
    path('Returnbook',views.Returnbook,name='Returnbook'),
    path('Setting',views.Setting,name='Setting')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)