# # inventory/admin.py
from django.contrib import admin
from inventory.models import Product, CustomUser,CRFQ

admin.site.site_header = "Inventory Admin"


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("product","Types_of_Cell", "Industry_Type", "HSN_Code")
    list_filter = ["UOM"]
    search_fields = ["Types_of_Cell"]

class CRFQAdmin(admin.ModelAdmin):
    model = CRFQ
    list_display = ("created_by","rfqid", "rfqorder", "product", "order_quantity","client","valid")
    list_filter = ["rfqid"]
    search_fields = ["product"]


class UserProfileAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('user_Type','department', 'name','phone', 'email','location','user_pic')
    list_filter = ["name"]
    search_fields = ["name"]



admin.site.register(Product, ProductAdmin)
admin.site.register(CRFQ, CRFQAdmin)
admin.site.register(CustomUser, UserProfileAdmin)


