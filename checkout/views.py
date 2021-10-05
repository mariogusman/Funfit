from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        #if theres nothing in users bag will redirect to /products
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JhEWLIZW5FlcMDW5UpW8tEIxS30FwkptHpSGm8hRJ63Y1HLdgOWEpNlhGlrqKkEAzj0JeilBWDXq63mYh8WFeAi00ALtDHJvL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)