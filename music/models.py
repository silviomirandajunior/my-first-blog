from django.conf import settings
from django.db import models
from django.utils import timezone


class Disciplina(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField(blank=True, null=True)
    professor = models.CharField(max_length=100, blank=True, null=True) ##chave estrangeira
    aluno = models.CharField(max_length=100, blank=True, null=True)   ##chave estrangeira
    
    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.titulo
        
class Professor(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    disciplina = models.CharField(max_length=100, blank=True, null=True)  ##chave estrangeira
    aluno = models.CharField(max_length=100, blank=True, null=True)      ##chave estrangeira
    
    
    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome
        
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    disciplina = models.CharField(max_length=100, blank=True, null=True) ##chave estrangeira
    professor = models.CharField(max_length=100, blank=True, null=True)  ##chave estrangeira
    
    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome