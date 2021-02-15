from django.contrib import admin
from .models import *


# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "description", "type", "price", "sale"]


class AboutUsPage(admin.ModelAdmin):
    list_display = ["title", "description"]


admin.site.register(Product, ProductsAdmin)
admin.site.register(Order)
admin.site.register(AboutUs, AboutUsPage)
admin.site.register([Contakts, Profile])
