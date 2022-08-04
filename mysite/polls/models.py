from django.db import models

# Create your models here.
# criando modelos dentro do banco de dados


class Pergunta(models.Model):  # criando a classe de pergunta
    pergunta_texto = models.CharField(max_length=200)  # tamanhao maximo
    pub_date = models.DateTimeField('data pub')  # data de publicação


class Alternativa(models.Model):
    # foreigkey relaciona a pergunta com com as alternativas, e o ondelete é pra quando apagar a pergunta apagar as alternativas tambem
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    alternativa_text = models.CharField(max_length=200)  # tamanho da pergunta
    votes = models.IntegerField(default=0)  # contador de votos
