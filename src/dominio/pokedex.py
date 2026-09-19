from src.dominio.__init__ import *

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

    def siguiente_evolucion(self, evoluciones, id_pokemon):  # A partir de un id_pokemon devuelve el      del que seria su version evolucionada

        if evoluciones == []:    #Caso base, si recorri todo entonces devolver none
            return None

        if evoluciones[0][0] == id_pokemon:
            return evoluciones[0][1]    # Resultado de la busqueda: Si encontre el id del pokemon entonces me devuelve el id del pokemon que va a evolucionar

        return self.siguiente_evolucion(evoluciones[1:], id_pokemon) #Caso recursivo: Sigo buscando pero descartando el primer array que ya analice.


        # cadena de evoluciones hacia adelante
    def cadena_evolucion(self, id_pokemon):

        if self.buscar_pokemon_por_id(id_pokemon) is None: # si no existe el id del pokemon : caso base -> Retornar un array vacio
            return []
        # None si no evoluciona
        if self.siguiente_evolucion(EVOLUCIONES, id_pokemon) is None: # Si no encontre una siguiente evolucion (Ver caso base de de siguiente_evolucion) retornar el parametro id_pokemon como un array
            return [id_pokemon]
        
        return [id_pokemon] + self.cadena_evolucion(self.siguiente_evolucion(EVOLUCIONES, id_pokemon)) # Agregar como array la ID
    
    def mostrar_cadena_de_evolucion(self, id_pokemon): # Muestra en el CLI el resultado 
        print(self.cadena_evolucion(id_pokemon))
    

