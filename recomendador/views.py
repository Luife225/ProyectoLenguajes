import requests
from django.shortcuts import render
from .models import Videojuego
from .processor import filtrar_videojuegos
from .logic import obtener_recomendacion_final

def home(request):
    api_key = "1c0ceafa6be94108aab04750092adbd7"
    url = f"https://api.rawg.io/api/games?key={api_key}&page_size=6"
    response = requests.get(url)
    data = response.json()
    games = data.get("results", [])
    return render(request, "home.html", {"games": games})

def index(request):
    if request.method == "POST":
        genero = request.POST.get("genero")
        plataforma = request.POST.get("plataforma")
        dificultad = request.POST.get("dificultad")

        videojuegos = Videojuego.objects.all()
        
        # Paradigma Funcional: Filtrado de datos
        filtrados = filtrar_videojuegos(videojuegos, genero, plataforma, dificultad)
        
        # Paradigma Lógico: Obtener recomendación destacada
        destacados = obtener_recomendacion_final(filtrados)

        return render(request, "resultado.html", {
            "videojuegos": filtrados,
            "destacados": destacados
        })
    
    return render(request, "index.html")
