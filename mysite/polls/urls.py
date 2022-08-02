from django.urls import path

from . import views #da minhas pasta polls, importe o arquivo views

#urlpatterns diz pra qual endereço url aquela função deve seguir

urlpatterns = [
    path('', views.index, name='index'),#como é um espaço vazio eu to definindo que é a raiz, e to dizendo que o caminho praquela função que criei é essa raiz
]