from django.shortcuts import render
from .models import Products

# Create your views here.
def all_products(request):
    # a view that shows all products and enables sorting and searching
    
    products = Products.objects.all()
    
    context = {
        'products' : products,
    }
    
    return render(request, 'products/products.html', context)