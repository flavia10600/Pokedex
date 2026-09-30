from src.excepciones import ColeccionLlenaError
from src.tads.cola import Cola
from src.dominio.pokedex import pokedex


class Equipo:
    def __init__(self, tope=6):
        self._pokemones = Cola() # Los pokemones estan en una cola, la cola ya crea una lista enlazada
        self._tope = tope

    def agregar(self, pokemon_id):
        #Obtener pokemon en forma de diccionario a traves del pokedex y agregarlo a la cola y la cola lo agrega en forma de lista enlazada

        if self._pokemones.tamanio_items() >= self._tope:
            raise ColeccionLlenaError(f"El equipo está lleno (máximo {self._tope}).")
        
        self._pokemones.encolar(pokedex.buscar_pokemon_por_id(pokemon_id))

    def eliminar(self, pokemon):
        self._pokemones.desencolar(pokemon)
        
    def listar(self):
        self._pokemones.mostrar_items()