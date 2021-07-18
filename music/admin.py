from django.contrib import admin
from .models import Disciplina, Aluno, Professor

admin.site.register(Disciplina)
admin.site.register(Aluno)
admin.site.register(Professor)