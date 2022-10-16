from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

import products
from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1>Welcome To The Website<h1>")


def get_product(request, product_id):
    products = Product.objects.get(id=product_id)
    context = {
        "product": {
            "name": products.name,
            "id": products.id,
            "description": products.description,
            "price": products.price,
        }
    }
    return render(request, "product-detail.html", context)


def get_products(request):
    products = Product.objects.all()
    thenew_product = []
    for product in products:
        thenew_product.append(
            {
                "name": products.name,
                "description": products.description,
                "price": products.price,
            }
        )
    context = {"products": thenew_product}
    return render(request, "product-list.html", context)
