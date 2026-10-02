from src.config import TEMA
from src.dominio.__init__ import * #Traigo el catalogo y las evoluciones
from src.dominio.equipo import Equipo
from src.dominio.pokedex import pokedex
from src.excepciones import ColeccionLlenaError, ColaVaciaError, PilaVaciaError
from src.tads.pila import Pila

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Evolucion de pokemon por ID (Operación recursiva)")  #Modificada la opcion del esqueleto para indicar que hace
    print("6. Colección principal (equipo)") # Modificada la opcion del esqueleto para indicar que hace
    print("7. Historial de pokemons en la pokedex (pila)") # Modificada la opcion del esqueleto para indicar que hace
    print("8. Cola de turnos de combate (Cola)") # Modificada la opcion del esqueleto para indicar que hace
    print("9. Guardar / cargar archivos")
    print("0. Salir")

def opcion_ocho(equipo: Equipo): # Esto esta hecho con IA. Yo se como funciona todo e hizo justo lo que yo iba a hacer, solo me ahorro el tiempo de hacerlo.
    # 8. Cola de turnos de combate (Cola) 
    print()
    print("=== Cola de turnos de combate ===")

    while True:
        print()
        print("1. Agregar pokemon al equipo")
        print("2. Quitar pokemon del equipo")
        print("0. Volver al menu principal")
        subopcion = input("> ").strip()

        if subopcion == "0":
            print("Volviendo al menu principal.")
            return

        # 1. Dar la opcion de elegir que pokemon elegir / Agregarlo y mostrar el equipo completo
        if subopcion == "1":
            print()
            print("El equipo actual es: ")
            equipo.listar()
            # 3. Indicar cuantos mas se pueden poner
            print(f"Pokemones en el equipo: {equipo.tamanio_equipo()} / {equipo.tope_equipo()}")
            print(f"Todavia se pueden poner {equipo.espacio_disponible()} pokemon/s.")

            try:
                id_pokemon = int(input("Escribir ID de pokemon: "))
                equipo.agregar_por_id(id_pokemon)
            except ColeccionLlenaError as error:
                # 2. Si son mas de 6 catch {error}
                print(f"Error: {error}")
                print(f"Quita un pokemon antes de agregar otro.")
            except ValueError:
                print("Error: el ID tiene que ser un numero entero.")
            else:
                print()
                print("El equipo actual es: ")
                equipo.listar()

        # 4. Quitarlo y mostrar el equipo completo -> Si no hay pokemon dar error
        elif subopcion == "2":
            try:
                quitado = equipo.quitar_del_frente()
            except ColaVaciaError as error:
                print(f"Error: {error}")
            else:
                print()
                print(f"Saca del equipo: {quitado.nombre} (ID {quitado.id})")
                print("El equipo actual es: ")
                equipo.listar()
                print(f"Todavia se pueden poner {equipo.espacio_disponible()} pokemon/s.")

        else:
            print("Opcion invalida.")

def opcion_siete():

    pokemons_apilados = Pila()
    print()
    print("=== Pila de visitas a pokemones ===")

    while True:
        print()
        print("1. Apilar pokemon")
        print("2. Desapilar pokemon")
        print("0. Volver al menu principal")

        subopcion = input("> ").strip()

        if subopcion == "0":
            print("Volviendo al menu principal.")
            return
        
        elif subopcion == "1":
            print()
            try:
                id_pokemon = int(input("Escribir ID de pokemon: "))
                pokemons_apilados.apilar(pokedex.buscar_pokemon_por_id(id_pokemon))
            except ValueError:
                print("Error: el ID tiene que ser un numero entero.")

            print("Pila actual es: ")
            pokemons_apilados.mostrar_items()

        elif subopcion == "2":
            try:
                pokemons_apilados.desapilar()
            except PilaVaciaError as error:
                print(f"Error: {error}")
                print(f"No se puede quitar pokemons en una pila vacia")

            print("Pila actual es: ")
            pokemons_apilados.mostrar_items()

        else:
            print("Opcion invalida")

def main():
    equipo = Equipo()
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            pokedex.listar_catalogo()
        elif opcion == "5":
            pokedex.mostrar_cadena_de_evolucion(172)
        elif opcion == "6": # 6. Colección principal (equipo)
            equipo.listar()
            # Mostrar el equipo actual -> Este equipo se modifica desde la cola de turnos de combate
        elif opcion == "7": # 7. Historial de pokemons en la pokedex (pila)
            opcion_siete()
            pass

        if opcion == "8": # 8. Cola de turnos de combate (Cola)
            opcion_ocho(equipo)
        elif opcion in {"2", "3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":#
    #equipo = Equipo()
    #equipo.agregar_por_id(172)
    #equipo.agregar_por_id(1)
    #equipo.agregar_por_id(11)
    #equipo.agregar_por_id(81)
    #equipo.agregar_por_id(92)
    #equipo.agregar_por_id(75)
    #equipo.agregar_por_id(76)
    #equipo.listar()
    main()

