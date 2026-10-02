from src.excepciones import ColeccionLlenaError
from src.tads.cola import Cola
from src.dominio.pokedex import pokedex


class Equipo: #Esto tambien es el equipo de combate
    def __init__(self, tope=6):
        self._pokemones = Cola() # Los pokemones estan en una cola, la cola ya crea una lista enlazada e indica tambien la cola de combate
        self._tope = tope

    def agregar_por_id(self, pokemon_id):
        #Obtener pokemon en forma de diccionario a traves del pokedex y agregarlo a la cola y la cola lo agrega en forma de lista enlazada

        if self._pokemones.tamanio_items() >= self._tope:
            raise ColeccionLlenaError(f"El equipo está lleno (máximo {self._tope}).")
        
        self._pokemones.encolar(pokedex.buscar_pokemon_por_id(pokemon_id))

    def eliminar(self, pokemon):
        self._pokemones.desencolar(pokemon)

    def quitar_del_frente(self):
        # Saca (desencola) al primero del equipo y lo devuelve. Si no hay, la Cola lanza ColaVaciaError.
        return self._pokemones.desencolar()

    def listar(self):
        self._pokemones.mostrar_items()

    def tamanio_equipo(self):
        return self._pokemones.tamanio_items()

    def tope_equipo(self):
        return self._tope

    def espacio_disponible(self): #Esto ayuda a saber cuanto falta antes de que se llene la cola
        return self._tope - self._pokemones.tamanio_items()