from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "categories"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products_images", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"