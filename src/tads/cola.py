from src.excepciones import ColaVaciaError
from src.tads.lista_enlazada import ListaEnlazada

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""
    def __init__(self):
        self._items = ListaEnlazada()

    def encolar(self, dato):
        self._items.insertar_al_final(dato)

    def desencolar(self):       
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")
        frente = self.ver_frente()
        self._items.eliminar(frente)
        return frente

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()