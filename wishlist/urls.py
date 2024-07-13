from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('delete/<int:wishlist_id>/', views.delete_wish, name='delete_wish'),
]
