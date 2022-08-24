from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render (request, "home.html",{})

def jonathan(request):
    
    return render (request, "paginas/Jonathan.html",{})

def Carlitos(request):

    return render (request, "paginas/Site-Old-Gamer/Site do Projeto/index.html",{})

def Carlitos1(request):

    return render (request, "paginas/Site-Old-Gamer/Site do Projeto/pag_01.html",{})

def Carlitos2(request):

    return render (request, "paginas/Site-Old-Gamer/Site do Projeto/pag_02.html",{})

def Carlitos3(request):

    return render (request, "paginas/Site-Old-Gamer/Site do Projeto/pag_3.html",{})

def Carlitoscao(request):

    return render (request, "paginas/Site-Old-Gamer/Site do Projeto/secao-img.html",{})

def Moises(request):
    
    return render (request, "paginas/moises.html",{})