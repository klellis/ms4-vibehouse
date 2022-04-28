from django.db import models

# Create your models here.
class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100)
    frontend_name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_frontend_name(self):
        return self.frontend_name
    
    
class Products(models.Model):
    class Meta:
        verbose_name_plural = 'Products'
        
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=30, null=True, blank=True)
    collection = models.CharField(max_length=70, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    
    
    def __str__(self):
        return self.name