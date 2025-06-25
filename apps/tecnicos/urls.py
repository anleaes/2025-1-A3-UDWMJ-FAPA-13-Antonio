from django.urls import path
from . import views

app_name = 'tecnicos'

urlpatterns = [
    path('', views.list_tecnicos, name='list_tecnicos'),
    path('adicionar/', views.add_tecnico, name='add_tecnico'),
    path('editar/<int:id_tecnico>/', views.edit_tecnico, name='edit_tecnico'),
    path('excluir/<int:id_tecnico>/', views.delete_tecnico, name='delete_tecnico'),
]