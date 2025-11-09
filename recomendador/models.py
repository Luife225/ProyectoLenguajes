from django.db import models

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    puntuacion = models.FloatField()
    dificultad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
