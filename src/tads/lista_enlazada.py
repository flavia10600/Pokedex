from src.tads.nodo import Nodo


class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""
    def __init__(self):
        self._cabeza = None # no hay nodos todavía
        self._tamanio = 0 # tamaño inicial: 0

    def esta_vacia(self):   # Podria ser una funcion privada porque se usa mas que nada para que funcionen otras funciones dentro de esta clase
        return self._cabeza is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
         # El nodo nuevo apunta al que era la cabeza, y después lo reemplaza.
         # usarlo solo si no es el ultimo nodo, en ese caso usar insertar_al_final()
        nuevo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        # Debe ser el ultimo nodo dentro de la lista porque agrega un none y no una referencia a otro nodo.
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamanio += 1

    def insertar_ordenado(self, dato, clave):   # Lo voy a crear cuando sea necesario
        raise NotImplementedError

    def eliminar(self, dato):
        if self.esta_vacia():
            return
        
        # Caso 1: es la cabeza
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.siguiente
            self._tamanio -= 1
            return
        
        # Caso 2: buscar el nodo anterior
        actual = self._cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                self._tamanio -= 1
                return
            actual = actual.siguiente
            

    def buscar(self, dato):
        actual = self._cabeza

        while actual is not None:
            if actual.dato == dato:
                return actual # lo encontró
            actual = actual.siguiente

        return None # no lo encontró

    def __iter__(self): #Convierte la lista enlazada en una clase iterable por el for while
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
