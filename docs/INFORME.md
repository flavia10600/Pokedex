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

Función: cadena_evolucion(pokedex, id). 
Caso base: si el Pokémon no tiene evolución siguiente → devolver [id]. 
Caso recursivo: [id] + cadena_evolucion(pokedex, siguiente)

Traza para Bulbasaur (id 1): según EVOLUCIONES, 1→2→3.

* Llamada 1: cadena_evolucion(1) → tiene siguiente (2) → devuelve [1] + cadena_evolucion(2)
* Llamada 2: cadena_evolucion(2) → tiene siguiente (3) → devuelve [2] + cadena_evolucion(3)
* Llamada 3: cadena_evolucion(3) → NO tiene siguiente (caso base) → devuelve [3]

Resultado: [1] + [2] + [3] = [1, 2, 3]

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada | insertar_al_inicio(dato), insertar_al_final(dato), eliminar(dato), buscar(dato), esta_vacia(), tamanio(), iter() |  |
| Pila | apilar(dato), desapilar(), ver_tope(), esta_vacia(), tamanio_items() |  |
| Cola | encolar(dato), desencolar(), ver_frente(), esta_vacia(), tamanio_items() |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

La complejidad es cómo crece el tiempo (y el espacio) que necesita una operación cuando crece el tamaño de la entrada, y se escribe con notación O(...) sin depender de la máquina.

n = cantidad de pokémons del catálogo (hoy 70) · m = filas de EVOLUCIONES · k = largo de la cadena de evolución.

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | O(n) | O(1) | Recorre los n elementos una vez con el iterador. |
| Buscar pokémon por ID (`buscar_pokemon_por_id`, E2; lo usan las opciones 5, 7 y 8) | O(1) mejor / O(n) peor | O(1) | Recorre el catálogo de a uno; si el id es del primero, sale enseguida. |
| Búsqueda lineal (nombre) | O(1) mejor / O(n) peor | O(1) | Toca cada elemento hasta encontrarlo o llegar al final; no usa `in` ni `index()`. Funciona con el catálogo en cualquier orden. |
| Búsqueda binaria (nombre) | O(log n) | O(1) | Cada comparación descarta la mitad del rango: como máximo log₂n pasos. Necesita el catálogo ordenado por nombre. |
| Ordenar por selección | O(n²) siempre | O(1) | Dos bucles anidados: (n−1) + (n−2) + ... + 1 ≈ n²/2 comparaciones, esté ordenado o no. |
| Ordenar por inserción | O(n) mejor / O(n²) peor y promedio | O(1) | Si ya está ordenado hace una comparación por elemento; si está al revés, desplaza todo. |
| Cadena de evolución (`cadena_evolucion`, E2) | O(k·(n+m)) | O(k) + las copias del slicing | Cada llamada busca el id en el catálogo (O(n)) y `siguiente_evolucion` recorre EVOLUCIONES cortando la lista (O(m) por nivel, y el corte copia); quedan k marcos de recursión. |
| Apilar / desapilar (pila) | O(1) | O(1) | Trabajan sobre la cabeza de la lista enlazada, sin recorrerla. |
| Encolar (cola) | O(n) | O(1) | `insertar_al_final` recorre la lista hasta el último nodo para engancharlo. |
| Desencolar (cola) | O(1) | O(1) | Saca la cabeza de la lista enlazada: no recorre nada. |

Mediciones (`time.perf_counter`):

Corridas en la máquina del grupo (i5-11400H, Windows 10, Python 3.11.15) sobre el catálogo completo (n = 70) y una copia ×10 (n = 700). Mediana de 200 corridas para las búsquedas y 20 para los ordenamientos.

| Operación | n | segundos |
| --- | --- | --- |
| búsqueda lineal (nombre, peor caso: no está) | 70 | 0.000007 |
| búsqueda lineal (n × 10) | 700 | 0.000062 |
| búsqueda binaria (nombre, peor caso: no está) | 70 | 0.000002 |
| búsqueda binaria (n × 10) | 700 | 0.000005 |
| ordenar por selección | 70 | 0.000451 |
| ordenar por selección (n × 10) | 700 | 0.047087 |
| ordenar por inserción (ya ordenado, mejor caso) | 70 | 0.000018 |
| ordenar por inserción (n × 10, ya ordenado) | 700 | 0.000190 |
| ordenar por inserción (al revés, peor caso) | 70 | 0.000547 |
| ordenar por inserción (n × 10, al revés) | 700 | 0.057162 |

Al agrandar el catálogo ×10, la binaria casi no cambia (×2,5, porque son log n pasos), la lineal crece con n (×9) y los ordenamientos se disparan al cuadrado (×104). La inserción sobre el catálogo ya ordenado es el único caso que crece lineal (×10), que es su mejor caso.

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
