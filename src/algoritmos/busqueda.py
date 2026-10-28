def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """Devuelve el elemento cuya clave coincide con 'clave', o None si no está.

    obtener_clave: función que recibe un elemento y devuelve la clave a comparar
    (ej: lambda p: p["nombre"]). Si es None, se compara el elemento entero.
    """
    for elemento in coleccion:
        if obtener_clave is None:
            if elemento == clave:
                return elemento
        elif obtener_clave(elemento) == clave:
            return elemento
    return None    # no encontrado: el CLI avisa, no explota


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """Búsqueda binaria. REQUIERE que la colección esté ordenada por obtener_clave."""
    izq = 0
    der = len(coleccion_ordenada) - 1
    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave(coleccion_ordenada[medio])
        if valor == clave:
            return coleccion_ordenada[medio]
        elif valor < clave:
            izq = medio + 1        # la clave está en la mitad derecha
        else:
            der = medio - 1        # la clave está en la mitad izquierda
    return None    # recorrimos todo el rango y no está
