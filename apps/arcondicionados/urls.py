from django.urls import path
from . import views

app_name = 'arcondicionados'

urlpatterns = [
    path('adicionar/', views.add_arcondicionado, name='add_arcondicionado'),
    path('', views.list_arcondicionados, name='list_arcondicionados'),
    path('editar/<int:id_arcondicionado>/', views.edit_arcondicionado, name='edit_arcondicionado'),
    path('excluir/<int:id_arcondicionado>/', views.delete_arcondicionado, name='delete_arcondicionado'),
]