from src.dominio.__init__ import *
#Todas las evoluciones hardcodeadas igual que se hizo con los pokemons en la variable CATALOGO. Hecho con IA para que sea mas rapido de crear.
EVOLUCIONES = [
    (1, 2),
    (2, 3),
    (4, 5),
    (5, 6),
    (7, 8),
    (8, 9),
    (10, 11),
    (11, 12),
    (16, 17),
    (17, 18),
    (19, 20),
    (172, 25),
    (25, 26),
    (35, 36),
    (37, 38),
    (43, 44),
    (44, 45),
    (58, 59),
    (63, 64),
    (64, 65),
    (66, 67),
    (67, 68),
    (74, 75),
    (75, 76),
    (81, 82),
    (92, 93),
    (93, 94),
    (129, 130),
    (133, 134),
    (133, 135),
    (133, 136),
    (147, 148),
    (148, 149),
    (152, 153),
    (153, 154),
    (155, 156),
    (156, 157),
    (175, 176),
    (179, 180),
    (180, 181),
    (246, 247),
    (247, 248),
]

class Pokedex:
    def __init__(self):
        self.lista_de_pokemons = CATALOGO   #Se hace una carga de los datos del catalogo de forma "hardcodeada" directamente de la variable CATALOGO
        pass

    def buscar_pokemon(self,id_pokemon): #Del array CATALOGO buscar y retornar el diccionario  que tenga el ID pedido sino None
        for dic_pokemon in self.lista_de_pokemon:
            if dic_pokemon["id"] == id_pokemon: 
                return dic_pokemon 
        return None

    def listar_catalogo(self):  #Es el print de todos los pokemons en el catalogo
        for item in self.lista_de_pokemons:
            print(f"{item['id']:>3}  {item['nombre']}")
            # Ejemplo de lo que imprime: 1 Bulbasaur (...) 248 Tyranitar
    
    def siguiente_evolucion(self, id_pokemon):
 
        pass
