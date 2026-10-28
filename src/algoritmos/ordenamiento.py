def ordenar_seleccion(coleccion, obtener_clave):
    """Ordena la colección in place por selección (ascendente). NO es estable."""
    n = len(coleccion)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if obtener_clave(coleccion[j]) < obtener_clave(coleccion[pos_min]):
                pos_min = j
        coleccion[i], coleccion[pos_min] = coleccion[pos_min], coleccion[i]
    return coleccion


def ordenar_insercion(coleccion, obtener_clave):
    """Ordena la colección in place por inserción (ascendente). SÍ es estable."""
    for i in range(1, len(coleccion)):
        actual = coleccion[i]
        j = i - 1
        while j >= 0 and obtener_clave(coleccion[j]) > obtener_clave(actual):
            coleccion[j + 1] = coleccion[j]    # desplazo el mayor a la derecha
            j -= 1
        coleccion[j + 1] = actual              # inserto el elemento en su lugar
    return coleccion
