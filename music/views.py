from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'music/pagina_inicial.html', {})
    
def sobre(request):
    return render(request, 'music/sobre.html', {})
    
def material(request):
    return render(request, 'music/material.html', {})
    
def contato(request):
    return render(request, 'music/contato.html', {})
    
def trabalhe_conosco(request):
    return render(request, 'music/trabalhe_conosco.html', {})
    
def professores(request):
    return render(request, 'music/professores.html', {})
    
def cursos_piano(request):
    return render(request, 'music/cursos_piano.html', {})

def cursos_teclado(request):
    return render(request, 'music/cursos_teclado.html', {})

def cursos_guitarra(request):
    return render(request, 'music/cursos_guitarra.html', {})

def cursos_violao(request):
    return render(request, 'music/cursos_violao.html', {})

def cursos_bateria(request):
    return render(request, 'music/cursos_bateria.html', {})

def cursos_baixo(request):
    return render(request, 'music/cursos_baixo.html', {})

def cursos_cordas(request):
    return render(request, 'music/cursos_cordas.html', {})

def cursos_metais(request):
    return render(request, 'music/cursos_metais.html', {})

def cursos_madeiras(request):
    return render(request, 'music/cursos_madeiras.html', {})

def cursos_canto(request):
    return render(request, 'music/cursos_canto.html', {})

def cursos_teoria_musical(request):
    return render(request, 'music/cursos_teoria_musical.html', {})
