# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback | pasa |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue | pasa |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa | pasa | En el caso de la recursion del pokedex cuando se pide la cadena de evoluciones da la cadena completa|
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | solo el ítem (caso base) | pasa | En el pokedex cuando se busca solo el ID del siguiente pokemon evolucionado|
| P05 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia | pasa |  |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | pasa |  |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | pasa |  |
| P08 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | pasa |  |
| P09 | E4 | Búsqueda lineal de un nombre que existe | nombre = Golem | lo encuentra | pasa | Opción 3 → 1 → `Golem`: muestra la ficha completa (ID 76) |
| P10 | E4 | Búsqueda lineal de un nombre que no existe | nombre = Mewtow | no encontrado, sin traceback | pasa | Opción 3 → 1 → `Mewtow`: imprime "No encontrado", sin traceback y el menú sigue |
| P11 | E4 | Búsqueda binaria con catálogo desordenado | nombre = Golem, sin ordenar antes | avisa o reordena; no da un falso hit | pasa | Opción 3 → 2: avisa "El catálogo no estaba ordenado por nombre: se ordenó automáticamente", reordena con inserción y encuentra el pokémon |
| P12 | E4 | Ordenar por un criterio y después por otro | nombre con selección, después hp con inserción | el orden cambia | pasa | Opción 4 → 1 → 1 (nombre, selección) y después 4 → 2 → 2 (hp, inserción): el listado cambia de orden las dos veces |
| P13 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
