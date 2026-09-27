
class Nodo:
    """Un eslabón de la cadena. Contiene un dato y la referencia al
    siguiente."""
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
