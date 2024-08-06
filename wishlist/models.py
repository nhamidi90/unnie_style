from django.db import models
from products.models import Product
from profiles.models import UserProfile


# Create your models here.
class Wishlist(models.Model):
    """Wishlist model"""
    products = models.ForeignKey(Product, null=True, blank=True,
                                 on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True,
                                     on_delete=models.CASCADE)
