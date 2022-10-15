from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1>Welcome To The Website<h1>")


def get_product(request, product_id):
    products = Product.objects.get(id=product_id)
    return HttpResponse(
        f"name:{products.name}, price:{products.price}, description:{products.description}"
    )
