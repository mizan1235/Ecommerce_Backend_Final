from django.contrib import admin
from Ecommerce.models import product_details,user_details,card,orders

# Register your models here.
admin.site.register(product_details)
admin.site.register(user_details)
admin.site.register(card)
admin.site.register(orders)