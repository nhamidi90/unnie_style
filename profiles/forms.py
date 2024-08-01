from django import forms
from .models import Addresses

class AddressForm(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = ('street_address1', 'street_address2', 'town_or_city', 
                  'county', 'postcode', 'country', 'default_address')
        widgets = {
            'default_address': forms.CheckboxInput()
        }


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
            'default_address': False,
        }

        self.fields['street_address1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            if field == 'default_address':
                self.fields[field].label = 'Set as default address'