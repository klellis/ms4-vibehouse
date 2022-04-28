import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Products

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False) #do not want order number to be editable as it is a unique identifier to each order
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email= models.EmailField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    street_address_1 = models.CharField(max_length=80, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, null=True, blank=True)
    town_city = models.CharField(max_length=40, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    
    def _create_order_number(self):
        # generates a random 32 char number using UUID 
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        #updates the total after each line item to take into account new delivery costs
        self.order_cost = self.lineitems.aggregate(Sum('item_total'))['item_total__sum']
        if self.order_cost < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_cost * settings.STANDARD_DELIVERY_PERCENT / 100
        else:
            self.delivery_cost = 0 
        self.grand_total = self.order_cost + self.delivery_cost
        self.save()
        
    
    def save(self, *args, **kwargs):
        #overrides the default save method to ensure order number is set
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.order_number
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Products, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product_size = models.CharField(max_length=2, null=True, blank=True)
    qty = models.IntegerField(null=False, blank=False, default=0)
    item_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)
    
    
def save(self, *args, **kwargs):
        #overrides the default save method to set item total
    
    self.item_total = self.product.price * self.qty
    super().save(*args, **kwargs)
        
        
def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'