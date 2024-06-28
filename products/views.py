from django.shortcuts import render, get_object_or_404
from .models import Product, OtherImages

# Create your views here.
def all_products(request):
    """ A view to return all products including sorting and searching """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    images = OtherImages.objects.all()

    context = {
        'product': product,
        'images': images,
    }
    
    return render(request, 'products/product_detail.html', context)