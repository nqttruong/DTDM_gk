from django.contrib import admin
from .models import Coffee
from .models import Order
# Register your models here.


class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Coffee, CoffeeAdmin) 
admin.site.register(Order)
