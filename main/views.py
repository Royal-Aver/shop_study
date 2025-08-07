from django.shortcuts import render

from products.models import Category


def index(request):
    categories = Category.objects.all()

    context = {
        'title': 'Главная',
        'header': 'Магазин компьютерных игр GAME ZONE',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'header': 'О нас',
        'description': 'Текст о том какой классный этот интернет магазин.'
    }
    return render(request, 'main/about.html', context)
