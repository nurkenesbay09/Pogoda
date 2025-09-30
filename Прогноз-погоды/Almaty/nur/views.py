from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return HttpResponse("<h5>Проверка работы</h5>")

def about (request):
    return HttpResponse("<h5>Страница про нас</h5>")