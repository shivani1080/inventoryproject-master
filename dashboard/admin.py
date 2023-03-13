from django.contrib import admin
from .models import Product,Issued_Items
from django.contrib.auth.models import Group
admin.site.site_header='CDAC INVENTORY DASHBOARD'
class productadmin(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=('category',)
# Register your models here.
admin.site.register(Product,productadmin)
admin.site.register(Issued_Items)
#admin.site.unregister(Group)
