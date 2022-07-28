from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, este é meu primeiro site Django")
