from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ View that returns the bag page """
    return render(request, 'bag/bag.html')
