from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = ("name", "price", "quantity")
    extra = 0


class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = ("user", "requires_delivery", "payment_on_get", "is_paid", "status")
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "delivery_address",
        "payment_on_get",
        "is_paid",
        "status",
        )
    search_fields = ("id",)
    list_filter = (
        "requires_delivery",
        "payment_on_get",
        "is_paid",
        "status",
    )

    inlines = [OrderItemTabularAdmin]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "name",
        "price",
        "quantity",
        "created_timestamp",)

    search_fields = ("name",)