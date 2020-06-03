from django.contrib import admin
from .models import Product, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """docstring for ProductAdmin."""
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)
