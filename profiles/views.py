from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import AddressForm


# Create your views here.
def profile(request):
    """ Display user's profile """
    form = AddressForm()    
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template, context)
