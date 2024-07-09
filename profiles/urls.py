from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/<int:address_id>/', views.edit_address, name='edit_address'),
    path('delete/<int:address_id>/', views.delete_address, name='delete_address'),
]
