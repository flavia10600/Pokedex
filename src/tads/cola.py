from src.excepciones import ColaVaciaError
from src.tads.lista_enlazada import ListaEnlazada

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""
    def __init__(self):
        self._items = ListaEnlazada()

    def encolar(self, dato):
        """Agrega al final de la cola."""
        self._items.insertar_al_final(dato)

    def desencolar(self):       
        """Sacá del frente. Si la cola está vacía, lanzá ColaVaciaError."""
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")
        frente = self.ver_frente()
        self._items.eliminar(frente)
        return frente

    def ver_frente(self):
        """Mirá el del frente sin sacarlo."""
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()

    def tamanio_items(self):
        return self._items.tamanio()

    def mostrar_items(self):
        for item in self._items:
            print(item)
            print("-------------")
