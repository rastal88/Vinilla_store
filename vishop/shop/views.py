from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = ["О сайте", "Каталог", "Обратная связь", "Войти"]


def index(request):
    cats = Product.objects.all()
    return render(request, 'shop/index.html', {'cats': cats, 'menu': menu, 'title': 'Главная страница'})


def pageNotFound(request, exception):
    return HttpResponseNotFound


def about(request):
    return render(request, 'shop/about.html', {'menu': menu, 'title': 'О сайте'})

