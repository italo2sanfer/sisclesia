from __future__ import unicode_literals

from django.db import models
from .choices import CATEGORIA_PESSOA
from .choices import BASE

class Pessoa(models.Model):
    categoria_pessoa = models.CharField(u'Categoria Pessoa', max_length=5,
        blank=True, choices=CATEGORIA_PESSOA)
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True, verbose_name=u'Email principal')
    data_nascimento = models.DateField()
    data_casamento = models.DateField()
    data_coonversao = models.DateField()
    data_batismo = models.DateField()
    aluno_ebd = models.BooleanField(default=False)
    observacao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Unidade(models.Model):
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.descricao


class Ministerio(models.Model):
    descricao = models.CharField(max_length=200)
    base = models.CharField(u'Base', max_length=5, blank=True, choices=BASE)
    uniadade = models.ForeignKey(Unidade)
    
    def __str__(self):
        return self.descricao


class Cargo(models.Model):
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.descricao


class Participacao(models.Model):
    ministerio = models.ForeignKey(Ministerio)
    cargo = models.ForeignKey(Cargo)
    pessoa = models.ForeignKey(Pessoa)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.CharField(max_length=200)
    
    def __str__(self):
        return self.descricao
