from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('admin/mabar/mabar/')),
    path('public/', include('mabar.urls')),
    path('public/', lambda request: redirect('list-mabar/')),
]
