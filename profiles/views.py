from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Addresses
from checkout.models import Order
from .forms import AddressForm


# Create your views here.
@login_required
def profile(request):
    """ Display user's profile and addresses including ability to add 
    new address"""
    profile = get_object_or_404(UserProfile, user=request.user)
    addresses = Addresses.objects.all()
    orders = profile.orders.all()

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid:
            form.save()

            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Unable to add address. Please try again')
    else:
        form = AddressForm()    
        
    
    template = 'profiles/profile.html'

    context = {
        'profile': profile,
        'addresses': addresses,
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)


@login_required
def edit_address(request, address_id):
    """ Edit an address """
    address = get_object_or_404(Addresses, pk=address_id)

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Unable to update address. Please try again')
    else:
        form = AddressForm(instance=address)

    template = 'profiles/edit_address.html'
    context = {
        'address': address,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_address(request, address_id):
    """ Delete an address """
    address = get_object_or_404(Addresses, pk=address_id)
    address.delete()
    return redirect(reverse('profile'))


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)