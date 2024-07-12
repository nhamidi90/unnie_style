from django.shortcuts import render

# Create your views here.
def wishlist(request):
    """ Display the user's wishlist"""
    template = "wishlist/wishlist.html"
    context = {

    }
    return render(request, template, context)