from src.dominio.__init__ import *
# Todas las evoluciones hardcodeadas igual que se hizo con los pokemons en la variable CATALOGO. Hecho con IA para que sea mas rapido de crear.
# Son arrays con arrays xq cada array de 2 valores implica que la primera pos es el id_pokemon actual y segunda pos indica el id_pokemon que va a evolucionar
EVOLUCIONES = [
    [1, 2],
    [2, 3],
    [4, 5],
    [5, 6],
    [7, 8],
    [8, 9],
    [10, 11],
    [11, 12],
    [16, 17],
    [17, 18],
    [19, 20],
    [172, 25],
    [25, 26],
    [35, 36],
    [37, 38],
    [43, 44],
    [44, 45],
    [58, 59],
    [63, 64],
    [64, 65],
    [66, 67],
    [67, 68],
    [74, 75],
    [75, 76],
    [81, 82],
    [92, 93],
    [93, 94],
    [129, 130],
    [133, 134],
    [133, 135],
    [133, 136],
    [147, 148],
    [148, 149],
    [152, 153],
    [153, 154],
    [155, 156],
    [156, 157],
    [175, 176],
    [179, 180],
    [180, 181],
    [246, 247],
    [247, 248],
]

class Pokedex:
    def __init__(self):
        self.lista_de_pokemons = CATALOGO   #Se hace una carga de los datos del catalogo de forma "hardcodeada" directamente de la variable CATALOGO
        pass

    ###################
    # [ ENTREGA 1 ] -> Modularizado en entrega 2
    ###################

    def listar_catalogo(self):  #Es el print de todos los pokemons en el catalogo
        for item in self.lista_de_pokemons:
            print(f"{item['id']:>3}  {item['nombre']}")
            # Ejemplo de lo que imprime: 1 Bulbasaur (...) 248 Tyranitar


    
    ###################
    # [ ENTREGA 2 ] -> Caso recursivo
    ###################

    def buscar_pokemon_por_id(self,id_pokemon): #Del array CATALOGO buscar y retornar el diccionario  que tenga el ID pedido sino None
        for dic_pokemon in self.lista_de_pokemons:
            if dic_pokemon["id"] == id_pokemon: 
                return dic_pokemon 
        return None

    def siguiente_evolucion(self, evoluciones,id_pokemon):  # A partir de un id_pokemon devuelve el      del que seria su version evolucionada

        if evoluciones == []:    #Caso base, si recorri todo entonces devolver none
            return None

        if evoluciones[0][0] == id_pokemon:
            return evoluciones[0][1]    # Resultado de la busqueda: Si encontre el id del pokemon entonces me devuelve el id del pokemon que va a evolucionar

        return self.siguiente_evolucion(self, evoluciones[1:],id_pokemon) #Caso recursivo: Sigo buscando pero descartando el primer array que ya analice.


        # cadena de evoluciones hacia adelante
    def cadena_evolucion(self,id_pokemon):

        if self.buscar_pokemon_por_id(id_pokemon) is None: # si no existe: caso base
            return []
        # None si no evoluciona
        if self.siguiente_evolucion(id_pokemon) is None: # CASO BASE: última evolución
            return [id_pokemon]
        
        return [id_pokemon] + self.cadena_evolucion(self.siguiente_evolucion(id_pokemon)) # CASO RECURSIVO

