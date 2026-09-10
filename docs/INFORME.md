# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: pokedex
- Por qué lo eligieron (5–8 líneas): 
Elegimos este tema porque, dentro de las tres opciones disponibles, la que más nos interesó fue la de Pokédex. 
El motivo principal es que nos rememora a nuestra infancia y, además, nos pareció la propuesta más entretenida, 
ya que conocemos a los personajes con los que vamos a trabajar y nos resulta interesante poder desarrollar el proyecto a partir de ellos.

## 2. Modelo

Cada ítem del catálogo es un Pokémon y cada uno contiene los siguientes atributos: 
{
    "id", 
    "nombre", 
    "tipo1", 
    "tipo2", 
    "hp", 
    "ataque", 
    "defensa", 
    "velocidad",
    "generacion". 
}
Todos estos datos son inmutables porque el pokedex solo muestra los datos cuando se los pide pero no los modifica.

Por ejemplo: la generación en la que apareció por primera vez es un dato que permanece en el tiempo y no se debe modificar, y los stats base (hp, ataque, defensa, velocidad) son fijos de cada pokemon. Si un Pokémon es de un solo tipo, `tipo2` queda vacío (`""`), pero eso no lo vuelve mutable: el que tiene un solo tipo nunca va a tener dos. 

Las estructuras mutables son la Pokédex y el Equipo, ya que su contenido y organización pueden modificarse: es posible agregar o quitar Pokémon, así como cambiar su orden, sin modificar los atributos propios de cada uno.

Relación entre catálogo, colección principal, pila y cola:
   El catálogo es el pokedex
   La colección principal es (por ahora) un equipo
   La pila (por ahora) usamos un historial de consultas
   La cola (por ahora) es la cola de combates que elija el usuario

Relaciones entre catálogo, colección principal, pila y cola

                Pokédex (todos los ítems)
                        │
                        ▼
         Equipo (ítems activos/gestionados)
                   ┌────┴────┐
                   ▼         ▼
                  Pila      Cola
            (Historial de  (Cola de
             consultas)     combate)



## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
