from django.db import models

# Create your models here.
class Category(models.Model):
    """Category model"""
    class Meta:
        verbose_name_plural='Categories'
    
    name = models.CharField(max_length=100, null=False, unique=True,
    blank=False,)
    friendly_name = models.CharField(max_length=150, null=True, blank=True,)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Product model"""
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_color = models.BooleanField(default=False, null=True, blank=True)
    main_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class OtherImages(models.Model):
    class Meta:
        verbose_name_plural = 'Other Images'
    """ Model for extra images """
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
            return self.image