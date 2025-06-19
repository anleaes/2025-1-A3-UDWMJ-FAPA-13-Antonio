from django.urls import path
from . import views

app_name = 'principais'

urlpatterns = [
    path('', views.principal, name='principal'),
]