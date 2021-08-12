from django.conf import settings
from django.db import models
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

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
        
class Contato(models.Model):

    email = forms.EmailField(required=True, label='Remetente')
    assunto = forms.CharField(required=True)
    texto = forms.CharField(widget=forms.Textarea, label='Mensagem')
    
    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.assunto

class TrabalheConosco(models.Model):

    nome = models.CharField()
    telefone = models.CharField()
    email = models.EmailField(required=True, label='Remetente')
    formacao = models.CharField(required=True)
    instrumento = models.CharField(required=True)
    comentario = models.CharField(widget=forms.Textarea, label='Mensagem')
    
    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome

class Professor(models.Model):

    nome = models.CharField(required=True)
    telefone = models.CharField(required=True, max_length=12)
    email = models.EmailField(required=True, label='Remetente')
    formacao = models.CharField(required=True)
    instrumento = models.CharField(required=True)
    comentario = models.CharField(widget=forms.Textarea, label='Mensagem')
    
    def cadastrar(self):
        self.save()

    def __str__(self):
        return self.nome
