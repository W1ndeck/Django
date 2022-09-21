from django.shortcuts import render
from django.http import HttpResponse #basicamente é a resposta do servidor aquela requisição


def index(request): #index é a raiz, request é a requisição para aquele app, essa função cria o index
    return HttpResponse("Olá, este é meu primeiro site Django") 
