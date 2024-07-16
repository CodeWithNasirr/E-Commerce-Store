from django.contrib import admin
from .models import Category,Product,Contact,Orders,OrderUpdate
# Register your models here.

admin.site.register(OrderUpdate)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(Product)
admin.site.register(Category)
