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
        'stripe_public_key': 'pk_test_51KthVfApZqtZnCG8uvvR3NKIyqP6fTYb5mjDryVMxXZF7RG0oErNr2yjIdG6QNY0xoS3MxhHp9nIbQaeQvqXLt7x00mNU9RYPr',
        'client_secret': 'sk_test_51KthVfApZqtZnCG8CIt6NgZrwR8fmcUla1fwTtZCYUouZduh3Tl2BDopzWSfynO3xqg0OWeIraQHycypmvu5GLPH00zLMz1aCE',
    }
    
    return render(request, template, context)