from django.urls import path
from . import views

urlpatterns = [
    path('list-mabar/', views.mabar_list, name='mabar_list'),
    path('list-free-skin/', views.bonus_skin_list, name='bonus_skin_list'),
    path('bonus-skin/add/', views.bonus_skin_create, name='bonus_skin_create'),
    path('bonus-skin/<int:pk>/edit/', views.bonus_skin_update, name='bonus_skin_update'),
    path('bonus-skin/<int:pk>/', views.bonus_skin_detail, name='bonus_skin_detail'),
    path('bonus-skin/<int:pk>/delete/', views.bonus_skin_delete, name='bonus_skin_delete'),
    path('list-req-hero/', views.request_hero_list, name='request_hero_list'),
    path('request-hero/add/', views.request_hero_create, name='request_hero_create'),
    path('request-hero/<int:pk>/edit/', views.request_hero_update, name='request_hero_update'),
    path('request-hero/<int:pk>/', views.request_hero_detail, name='request_hero_detail'),
    path('request-hero/<int:pk>/delete/', views.request_hero_delete, name='request_hero_delete'),
    # CRUD for Mabar (login required)
    path('mabar/add/', views.mabar_create, name='mabar_create'),
    path('mabar/<int:pk>/edit/', views.mabar_update, name='mabar_update'),
    path('mabar/<int:pk>/', views.mabar_detail, name='mabar_detail'),
    path('mabar/<int:pk>/delete/', views.mabar_delete, name='mabar_delete'),
]
