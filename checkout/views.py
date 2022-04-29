from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe
# Create your views here.

# checks if bag is empty before directing to checkout if not triggers a toast error message
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oops! There's nothing in your bag right now")
        return redirect('products')
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KthVfApZqtZnCG8uvvR3NKIyqP6fTYb5mjDryVMxXZF7RG0oErNr2yjIdG6QNY0xoS3MxhHp9nIbQaeQvqXLt7x00mNU9RYPr',
        'client_secret': 'test secret key',
    }
    return render(request, template, context)