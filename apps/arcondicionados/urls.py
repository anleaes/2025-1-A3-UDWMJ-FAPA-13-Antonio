from django.urls import path
from . import views

app_name = 'arcondicionados'

urlpatterns = [
    path('adicionar/', views.add_arcondicionado, name='add_arcondicionado'),
    path('', views.list_arcondicionados, name='list_arcondicionados'),
]