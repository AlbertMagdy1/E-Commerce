from django.contrib import admin
from .models import Products,Order
# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "E-commerce Site"
admin.site.index_title = "Manage E-commerce Site"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price','discount_price', 'category', 'description')
    search_fields = ('title',)
    list_editable = ('price',)
    

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)