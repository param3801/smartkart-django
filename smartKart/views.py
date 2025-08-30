from django.shortcuts import render
from stores.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)
    for product in products:
        print(product.images.url)
    context = {'products': products}
    return render(request, 'home.html', context) 