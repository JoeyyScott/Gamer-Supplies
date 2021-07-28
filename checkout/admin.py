from django.contrib import admin
from .models import Order, CrateItems


class CrateItemsAdminInline(admin.TabularInline):
    model = CrateItems
    readonly_fields = ('crateitem_total',)
    list_display = ('supply', )


class OrderAdmin(admin.ModelAdmin):
    inlines = (CrateItemsAdminInline,)
    readonly_fields = ('order_number', 'date', 'order_total')

    fields = ('date', 'order_number', 'full_name', 'email',
              'contact_number', 'address_line_1', 'address_line_2',
              'town_or_city', 'county', 'postcode', 'country', )

    list_display = ('order_number', 'date', 'order_total',
                    'full_name', 'email',)

admin.site.register(Order, OrderAdmin)