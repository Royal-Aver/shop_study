from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from django.core.exceptions import ValidationError

from orders.forms import CreateOrderForm
from carts.models import Cart
from orders.models import Order, OrderItem


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if not cart_items.exists():
                        messages.warning(request, "Ваша корзина пуста")
                        return redirect('order:create')

                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=form.cleaned_data['requires_delivery'],
                        delivery_address=form.cleaned_data['delivery_address'],
                        payment_on_get=form.cleaned_data['payment_on_get']
                    )

                    for cart_item in cart_items:
                        product = cart_item.product
                        name = cart_item.product.title
                        price = cart_item.product.sell_price()
                        quantity = cart_item.quantity

                        if product.quantity < quantity:
                            messages.warning(request, f"{cart_item} недостаточно на складе")
                            raise ValidationError(
                                f"Недостаточно товара {name} на складе. \
                                    В наличии: {product.quantity}"
                            )

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity
                        )

                        product.quantity -= quantity
                        product.save()

                        cart_item.delete()

                    messages.success(request, "Заказ успешно оформлен")
                    return redirect("user:profile")

            except ValidationError as e:
                messages.warning(request, e)
                return redirect("orders:create")

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'phone_number': request.user.phone_number or ''
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'form': form,
        'order': True,
    }

    return render(request, 'orders/create_order.html', context)
