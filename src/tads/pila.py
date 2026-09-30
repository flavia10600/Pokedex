from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError

# Se tiene que usar esta clase para manejar la creacion y poner nodos dentro de la lista enlazada.
class Pila: 
    """Pila implementada sobre ListaEnlazada (LIFO)."""
    def __init__(self):
        self._items = ListaEnlazada()

    def apilar(self, dato):
        """Agrega al tope. Equivale a insertar_al_inicio en la lista."""
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        """Sacá el tope. Si la pila está vacía, lanzá PilaVaciaError."""
        if self.esta_vacia():
            raise PilaVaciaError("No hay elementos para deshacer.")
        tope = self.ver_tope()
        self._items.eliminar(tope)
        return tope

    def ver_tope(self):
        """Mirá el del tope sin sacarlo."""
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()

    def tamanio_items(self):
        return self._items.tamanio()
        
