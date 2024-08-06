from django.contrib import admin
from .models import Addresses, UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone_number',
    )


class AddressesAdmin(admin.ModelAdmin):
    list_display = (
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'postcode',
        'country',
        'default_address',
    )


admin.site.register(Addresses, AddressesAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
