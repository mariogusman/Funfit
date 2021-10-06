from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    #these are calculated by model methods - readonly to avoid tampering with
    readonly_fields = ('order_number', 'date','delivery_cost', 'order_total',
                       'grand_total', 'original_bag','stripe_pid')

    #allow me to specify the order of the fields in the admin interface
    fields = ('order_number', 'date', 'full_name','email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1','street_address2', 'county',
              'delivery_cost','order_total', 'grand_total', 'original_bag','stripe_pid')

    #restrict the cols that show in the order list
    list_display = ('order_number', 'date', 'full_name','order_total', 'delivery_cost',
                    'grand_total',)

    #brings most recent orders on the top
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)