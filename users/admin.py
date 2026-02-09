from django.contrib import admin

from orders.admin import OrderTabularAdmin
from users.models import User
from carts.models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ("product", "quantity", "created_timestamp")
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_displaay = ("username", "first_name", "last_name")

    inlines = (CartTabAdmin, OrderTabularAdmin)
