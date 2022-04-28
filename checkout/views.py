from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

#checks if bag is empty before directing to checkout if not triggers a toast error message
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oops! There's nothing in your bag right now")
        return redirect('products')
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    
    return render(request, template, context)