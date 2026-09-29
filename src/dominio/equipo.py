from src.excepciones import ColeccionLlenaError
from src.tads.lista_enlazada import ListaEnlazada


class Equipo:
    def __init__(self, tope=6):
        self._pokemones = ListaEnlazada()
        self._tope = tope

    def agregar(self, pokemon):
        if self._pokemones.tamanio() >= self._tope:
            raise ColeccionLlenaError(f"El equipo está lleno (máximo{self._tope}).")
        self._pokemones.insertar_al_final(pokemon)

    def eliminar(self, pokemon):
        self._pokemones.eliminar(pokemon)
        
    def listar(self):
        for p in self._pokemones:
            print(f" {p}")