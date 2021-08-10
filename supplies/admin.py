from django.contrib import admin
from .models import Category, Supply


# Supply model in admin
class SupplyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'brand')
    list_filter = ('category', 'brand')
    search_fields = (
        'name',
        'brand',
        'category__name',)


# Category model in admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Supply, SupplyAdmin)
