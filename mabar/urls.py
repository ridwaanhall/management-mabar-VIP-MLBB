from django.urls import path
from . import views

urlpatterns = [
    path('antri-mabar/', views.mabar_list, name='mabar_list'),
    path('bonus-skin/', views.bonus_skin_list, name='bonus_skin_list'),
    path('request-hero/', views.request_hero_list, name='request_hero_list'),
]
