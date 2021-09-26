from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ Shows all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ Shows  products details """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products.html', context)