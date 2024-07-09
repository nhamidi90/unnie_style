from django.contrib import admin
from .models import Addresses

# Register your models here.
class AddressesAdmin(admin.ModelAdmin):
    list_display = (
        'street_address1', 
        'street_address2', 
        'town_or_city', 
        'county', 
        'postcode', 
        'country',
        'default_address'
    )

admin.site.register(Addresses, AddressesAdmin)