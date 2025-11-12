import requests
from django.shortcuts import render
from .processor import filtrar_videojuegos
from .logic import obtener_recomendacion_final

API_KEY = "1c0ceafa6be94108aab04750092adbd7"
API_URL = "https://api.rawg.io/api/games"

def fetch_games_from_api(params={}):
    default_params = {"key": API_KEY, "page_size": 4}
    all_params = {**default_params, **params}
    try:
        response = requests.get(API_URL, params=all_params)
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException:
        return []

def home(request):
    games = fetch_games_from_api({"page_size": 6})
    return render(request, "home.html", {"games": games})

def index(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        genero = request.POST.get("genero")
        plataforma = request.POST.get("plataforma")

        search_params = {}
        if nombre:
            search_params["search"] = nombre
        if genero:
            search_params["genres"] = genero
        if plataforma:
            search_params["platforms"] = plataforma

        videojuegos = fetch_games_from_api(search_params)
        
        destacados = obtener_recomendacion_final(videojuegos)

        return render(request, "resultado.html", {
            "videojuegos": videojuegos,
            "destacados": destacados
        })
    
    return render(request, "index.html")


