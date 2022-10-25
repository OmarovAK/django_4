from django.shortcuts import render
from .models import Article


def list_pages_view(request):
    my_list = {
        'title': 'Главная страница'
    }
    return render(request, 'article/list_pages.html', my_list)

def article_view(request):
    my_list = {
        'title': 'Страница со статьями',
        'posts': Article.objects.all(),
    }

    return render(request, 'article/index.html', my_list)
