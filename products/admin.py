from django.contrib import admin

from products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    list_display = ("name",)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_display = ("title", "category", "price", "discount")
    list_editable = ("discount",)
    search_fields = ("title", "description")
    list_filter = ("price", "discount")
    fields = ("title", "category", "slug", ("price", "discount"), "description", "quantity", "image", )
