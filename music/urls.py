from django.urls import path
from . import views
from .views import ContatoCreate, TrabalheConoscoCreate, ProfessorCreate

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('sobre/', views.sobre, name='sobre'),
    path('material/', views.material, name='material'),
    path('contato/', views.contato, name='contato'),
    path('trabalhe_conosco/', TrabalheConoscoCreate.as_view(), name='trabalhe_conosco'),
    path('professores/', ProfessorCreate.as_view(), name='professores'),
    path('cursos/piano', views.cursos_piano, name='cursos_piano'),
    path('cursos/teclado', views.cursos_teclado, name='cursos_teclado'),
    path('cursos/violao', views.cursos_violao, name='cursos_violao'),
    path('cursos/guitarra', views.cursos_guitarra, name='cursos_guitarra'),
    path('cursos/baixo', views.cursos_baixo, name='cursos_baixo'),
    path('cursos/bateria', views.cursos_bateria, name='cursos_bateria'),
    path('cursos/cordas', views.cursos_cordas, name='cursos_cordas'),
    path('cursos/metais', views.cursos_metais, name='cursos_metais'),
    path('cursos/madeiras', views.cursos_madeiras, name='cursos_madeiras'),
    path('cursos/canto', views.cursos_canto, name='cursos_canto'),
    path('cursos/teoria_musical', views.cursos_teoria_musical, name='cursos_teoria_musical'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup')
]