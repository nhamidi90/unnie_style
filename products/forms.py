from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, OtherImages


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    main_image = forms.ImageField(
        label='', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_name


class OtherImagesForm(forms.ModelForm):

    class Meta:
        model = OtherImages
        fields = "__all__"

    image = forms.ImageField(
        label='Other Images', required=False, widget=CustomClearableFileInput)


# class EditImagesForm(forms.ModelForm):

#     class Meta:
#         model = OtherImages
#         exclude = ('product',)

#     image = forms.ImageField(label='', required=False,
#                              widget=CustomClearableFileInput)
