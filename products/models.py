from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "categories"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, verbose_name="Цена")
    discount = models.PositiveIntegerField(default=0, verbose_name="Скидка")
    description = models.TextField(verbose_name="Описание")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    image = models.ImageField(upload_to="products_images", blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        db_table = "products"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("id",)

    def __str__(self):
        return f"{self.title} | {self.price}"

    def display_id(self):
        return f"{self.id:07}"

    def sell_price(self):
        if self.discount:
            return self.price - (self.price * self.discount / 100)
        return self.price

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})