from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/<int:address_id>/', views.edit_address, name='edit_address'),
]
