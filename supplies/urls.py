from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_supplies, name='supplies'),
    path('add/', views.supply_add, name='supply_add'),
    path('edit/<int:supply_id>/', views.supply_edit, name='supply_edit'),
]
