from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Products, Category
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Products.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_nameLower('name'))
                # the below allows to sort by name rather than id so its more user friendly
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Ooops! Looks like you didn't enter anything.")
                return redirect('products')
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    sorting_by = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories' : categories,
        'sorting_by': sorting_by,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    # a view that shows individual product detail 
    product = get_object_or_404(Products, pk=product_id)
    
    context = {
        'product' : product,
    }
    
    return render(request, 'products/product_details.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
