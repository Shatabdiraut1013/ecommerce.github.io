from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate

admin.site.register(Product)  # means product ko register kar do..
admin.site.register(Contact)  # means contact ko register kar do..
admin.site.register(Orders)  # means Orders ko register kar do..
admin.site.register(OrderUpdate)  # means Orderupdate  ko register kar do..
