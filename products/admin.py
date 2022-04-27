from django.contrib import admin
from .models import Products, Category

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price', 
        'description', 
        'collection', 
        'image', 
        'rating',
        'sku',
    )
    
    ordering = ('sku',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'frontend_name', 
        'name',
    )
    
    
admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)