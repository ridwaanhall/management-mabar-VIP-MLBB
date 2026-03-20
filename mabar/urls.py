from django.urls import path
from . import views

urlpatterns = [
    path('list-mabar/', views.mabar_list, name='mabar_list'),
    path('list-free-skin/', views.bonus_skin_list, name='bonus_skin_list'),
    path('list-req-hero/', views.request_hero_list, name='request_hero_list'),
    # CRUD for Mabar (login required)
    path('mabar/add/', views.mabar_create, name='mabar_create'),
    path('mabar/<int:pk>/edit/', views.mabar_update, name='mabar_update'),
    path('mabar/<int:pk>/delete/', views.mabar_delete, name='mabar_delete'),
]
