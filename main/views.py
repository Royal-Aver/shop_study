from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная',
        'header': 'Магазин компьютерных игр GAME ZONE',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'header': 'О нас',
        'description': 'Текст о том какой классный этот интернет магазин.'
    }
    return render(request, 'main/about.html', context)
