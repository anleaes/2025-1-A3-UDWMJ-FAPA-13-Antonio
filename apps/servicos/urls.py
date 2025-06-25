from django.urls import path
from . import views

app_name = 'servicos'

urlpatterns = [
    path('', views.list_servico, name='list_servico'),
    path('adicionar/', views.add_servico, name='add_servico'),
    path('editar/<int:id_servico>/', views.edit_servico, name='edit_servico'),
    path('excluir/<int:id_servico>/', views.delete_servico, name='delete_servico'),

]