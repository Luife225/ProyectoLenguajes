def obtener_recomendacion_final(videojuegos):
    """
    Retorna una lista de nombres de videojuegos con una puntuación de 9 o más.
    Esta es una implementación simple sin pyDatalog para depuración.
    """
    recomendados = [v.nombre for v in videojuegos if v.puntuacion >= 9]
    return recomendados
