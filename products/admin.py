from django.contrib import admin
from .models import Product, Category, OtherImages

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(OtherImages)
