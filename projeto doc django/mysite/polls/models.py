from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
# criando modelos dentro do banco de dados


class Pergunta(models.Model):  # criando a classe de pergunta
    pergunta_texto = models.CharField(max_length=200)  # tamanhao maximo
    pub_date = models.DateTimeField('data pub')  # data de publicação

    def __str__(self): #este metodo(estudar POO em Python!!) serve para no shell ao inves de retornar só o ID retornar a pergunta
        return self.pergunta_texto

    def was_published_recently(self): #verifica se a pergunta foi adicionada a um dia
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Alternativa(models.Model):
    # foreigkey relaciona a pergunta com com as alternativas, e o ondelete é pra quando apagar a pergunta apagar as alternativas tambem
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    alternativa_text = models.CharField(max_length=200)  # tamanho da pergunta
    votes = models.IntegerField(default=0)  # contador de votos
    def __str__(self):
        return self.alternativa_text