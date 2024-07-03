from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents"""

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ A view to add specified product and quantity to bag"""

    product = get_object_or_404(Product, pk = item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if 'product_color' in request.POST:
        color = request.POST['product_color']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'‎')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'‎')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'‎')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'‎')
        else:
            bag[item_id] = quantity
            messages.success(request, f'‎')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the bag """

    product = get_object_or_404(Product, pk = item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove item from the bag"""

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'There was a problem removing your item {e}')
        return HttpResponse(status=500)