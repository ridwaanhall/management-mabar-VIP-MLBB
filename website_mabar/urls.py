from django.contrib import admin
from django.urls import path
from .views import redirect_to_mabar_admin

urlpatterns = [
    path('', redirect_to_mabar_admin),
    path('admin/', admin.site.urls),
]
