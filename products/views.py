from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, OtherImages, Category
from profiles.models import UserProfile
from wishlist.models import Wishlist
from .forms import ProductForm, OtherImagesForm


# Create your views here.
def all_products(request):
    """ A view to return all products including sorting and searching """

    products = Product.objects.all()

    query = None
    category = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search criteria")
                return redirect(reverse('products'))

            Queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(Queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
        'current_sorting': current_sorting,
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


@login_required
def add_product(request):
    """ Add a new product to the database """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add a product')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request, ''' Product could not be added. Please make
                sure the form is valid''')
    else:
        form = ProductForm()

    template = 'products/add_product.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_product_image(request):
    """ Add product image """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add a product')
        return redirect(reverse('home'))

    if request.method == 'POST':
        image_form = OtherImagesForm(request.POST, request.FILES)
        if image_form.is_valid():
            image_form.save()
            messages.success(request, 'Successfully added image')
            return redirect(reverse('products'))
        else:
            messages.error(
                request, '''Images could not be added. Please make
                sure the form is valid''')
    else:
        image_form = OtherImagesForm()

    template = 'products/add_product_image.html'

    context = {
        'image_form': image_form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can edit a product')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, '''Product could not be updated. Please make
                sure the form is valid''')
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'

    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product """

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can delete a product')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')

    return redirect(reverse('products'))


@login_required
def add_to_wishlist(request, product_id):
    """ Add product to user's wishlist """
    profile = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    if Wishlist.objects.filter(
            user_profile=profile, products=product).exists():
        messages.error(
            request, 'You have already added this item to your wishlist')
        return redirect(reverse('products'))
    else:
        Wishlist.objects.create(user_profile=profile, products=product)
        messages.success(
            request, f'Successfully added {product.name} to your wishlist')

    return redirect(reverse('wishlist'))
