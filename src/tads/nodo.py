
class Nodo:
    """Un eslabón de la cadena. Contiene un dato y la referencia al
    siguiente."""
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    # Funciones creadas para debugear
    def get_siguiente(self):
        return self.siguiente

    def get_dato(self):
        return self.dato
