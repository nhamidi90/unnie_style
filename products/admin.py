from django.contrib import admin
from .models import Product, Category, OtherImages

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'main_image',
    )
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'product',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OtherImages, ImageAdmin)
