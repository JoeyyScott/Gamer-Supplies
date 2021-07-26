from django.contrib import admin
from .models import Category, Supply


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


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Supply, SupplyAdmin)
