def filtrar_videojuegos(videojuegos, genero, plataforma, dificultad):
    filtrados = videojuegos
    if genero:
        filtrados = filter(lambda v: genero.lower() in v.genero.lower(), filtrados)
    if plataforma:
        filtrados = filter(lambda v: plataforma.lower() in v.plataforma.lower(), filtrados)
    if dificultad:
        filtrados = filter(lambda v: dificultad.lower() in v.dificultad.lower(), filtrados)
    return list(filtrados)
