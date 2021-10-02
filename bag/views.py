from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ View that returns the bag page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Adds a qty of the desired product to the user's bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # if the item is already in the bag will add to that quantity
    # else, if not in the bag, it will add that specified quantity
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)