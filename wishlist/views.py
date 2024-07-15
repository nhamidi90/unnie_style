from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from profiles.models import UserProfile

# Create your views here.
@login_required
def wishlist(request):
    """ Display the user's wishlist"""

    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user_profile=profile)

    template = "wishlist/wishlist.html"
    context = {
        'profile': profile,
        'wishlist': wishlist,
    }
    return render(request, template, context)


def delete_wish(request, wishlist_id):
    """ Delete item from wishlist """
    
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id)
    wishlist.delete()

    return redirect(reverse('wishlist'))
