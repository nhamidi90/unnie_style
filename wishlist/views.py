from django.shortcuts import render, get_object_or_404
from .models import Wishlist
from profiles.models import UserProfile

# Create your views here.
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