# Declaración de uso de IA

Actualizar **en cada entrega**. Si no usaron IA, dejar una fila que lo diga. No declarar cuando sí se usó anula la entrega.

Fecha de esta versión del archivo: 28/10/2026

| Entrega | Fecha | Herramienta (ChatGPT, Cursor, Copilot, otra) | Para qué (diseño, código, debug, docs) | Qué pegaron o generaron | Qué reescribieron / revisaron a mano | Integrante |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | 08/09 | deepseek | codigo | Todo el catalogo del .csv en una variable CATALOGO en el archivo __init__.py en la carpeta src/dominio | Probamos si se veian todos los pokemones | Leonardo Pezoa |
| E2 | 19/09 | ChatGPT | debug, docs, codigo |- Me ayudo a buscar errores cuando hacia recursiones y si aparecian errores en consola a leerlos y entenderlos. Mejoro la legibilidad del informe donde se explica la trazabilidad. Creo toda las lista de EVOLUCIONES en las que basandose en el archivo evoluciones.csv creo una lista de listas. A partir de la variable CATALOGO creo la clase que se encuentra en pokemon.py | Cuando se encontraba algun error de concepto que me indicaba la IA yo escribia a mano el codigo de las recursiones | Leonardo Pezoa |
| E3 | 04/10 | Deepseek | Codigo, debug, diseño | Creo las funciones opcion_ocho() y opcion_cinco() para poder hacer mas ordeando el codigo dentro del menu. Me ayudo a entender como funciona __ iter __. Pude aprender como pasar los elementos de un diccionario a los atributos de una clase con desempaquetado de diccionarios usando dos asteriscos (**). Aprendi a escribir en python un singleton que use en Pokedex. Tambien creo el __ str __ en la clase pokemon   | En el caso de los metodos yo ya los habia escrito a mano pero la IA los mejoro para que se vean mas ordenados en la consola. Lo demas fue conocimiento conceptual que aplique en el codigo a mano | Leonardo Pezoa |
| E4 | 28/10 | Deepseek (agente Hermes) | código, docs | Generó los cuatro algoritmos propios de src/algoritmos/ (busqueda_lineal, busqueda_binaria, ordenar_seleccion, ordenar_insercion), el estado que recuerda por qué criterio quedó ordenado el catálogo y las opciones 3 (Buscar) y 4 (Ordenar) del menú en main.py. También la tabla de complejidad y la de mediciones de docs/INFORME.md §5 y los casos P09–P12 del protocolo. | Revisé el código contra la guía (cotas, estabilidad, que no quede ningún sorted / list.sort / bisect), corrí el menú completo y las pruebas P09–P12, corrí las mediciones con time.perf_counter en mi máquina y ajusté a mano la redacción del informe. | Leonardo Pezoa |
| E5 |  |  |  |  |  |  |
| E6 |  |  |  |  |  |  |

Compromiso: cualquiera del grupo puede explicar cualquier archivo del tag.
