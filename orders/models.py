from django.db import models

from users.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пользователь")
    created_timestap = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")
    requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки")
    payment_on_get = models.BooleanField(default=False, verbose_name="Оплата при получении")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачен")
    status = models.CharField(max_length=50, default="В обработке", verbose_name="Статус")

    class Meta:
        db_table = "orders"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.pk} | {self.user.first_name} {self.user.last_name}"


class OrderItemQerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True, verbose_name="Товар")
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    objects = OrderItemQerySet.as_manager()

    class Meta:
        db_table = "order_items"
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def products_price(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        return f"{self.name} | Количество: {self.quantity} | заказ № {self.order.pk}"