# Entrega 1 — repo y catálogo vivo

**Vence:** domingo 06-sep-2026 23:59 · **Peso:** 5 % · Tag: `entrega-1`

Objetivo: dejar el primer repo **funcional** del grupo: clonable, con tema elegido, con un catálogo armado a mano en el código y un CLI mínimo que lista el catálogo. Los archivos `.txt` de `data/` quedan disponibles pero se empiezan a leer recién en E5; en E1 no se tocan. Si el repo no clona o el CLI no arranca, parte de la entrega se cae.

## 1. Mail

**Si no mandaron el mail del grupo (Armado), todavía están a tiempo:** primero va ese. Después el mail de la entrega, con el tag ya pusheado.

```text
Para: diego.ambrossio@unab.edu.ar; angel.bianco@unab.edu.ar
Asunto: AyED C2 2026 Comision 1 - GRUPO 04 - Entrega 1

Repo: https://github.com/comision1-grupo4/ayed-2026-recetario
Entrega de E1: esqueleto clonado, tema en config.py, catálogo armado
a mano, CLI que lista el catálogo, README con integrantes e informe
arrancado. Tag: entrega-1.
```

## 2. Qué tiene que tener el repo

| # | Ítem | Qué vas a mostrar |
| --- | --- | --- |
| 1.1 | README con integrantes, mails, tema y cómo ejecutar | `README.md` completo (tabla de integrantes + tema + `python -m src.main`) |
| 1.2 | Catálogo del tema presente, armado a mano en el código | una lista o diccionario en `src/dominio/` con los ítems del tema |
| 1.3 | CLI que lista el catálogo | `python -m src.main` → opción 1 imprime el catálogo completo |
| 1.4 | Funciones con responsabilidad clara | `main` no concentra la lógica; cada acción es una función |
| 1.5 | Informe arrancado | `docs/INFORME.md` §1 (por qué el tema) y §2 (qué es mutable/inmutable) |
| 1.6 | Declaración de IA presente | `docs/DECLARACION_IA.md` con una fila, aunque diga "no usamos" |

## 3. Ejemplo corto

`src/config.py` — tema elegido y no se cambia más:

```python
TEMA = "recetario"   # "pokedex" | "recetario" | "musica"
```

`src/dominio/receta.py` — el catálogo se arma en el código (los `.txt` se leen recién en E5):

```python
CATALOGO = [
    {"id": 1, "nombre": "Chimichurri", "tiempo_min": 15, "dificultad": "baja"},
    {"id": 2, "nombre": "Salsa criolla", "tiempo_min": 20, "dificultad": "baja"},
    {"id": 3, "nombre": "Sofrito", "tiempo_min": 25, "dificultad": "baja"},
]

def listar_catalogo():
    for item in CATALOGO:
        print(f"{item['id']:>3}  {item['nombre']}")
```

El menú (`src/main.py`) puede quedar tan simple como:

```text
=== Recetario — AyED C2 2026 ===
1. Listar catálogo
2. Ver detalle
...
```

## 4. Estructura sugerida del repo

Para esta entrega alcanza con esto (la estructura va a **crecer** en las próximas):

```text
ayed-2026-recetario/
├── README.md            # integrantes, tema, cómo ejecutar
├── src/
│   ├── config.py        # TEMA
│   ├── main.py          # menú + opción listar
│   ├── excepciones.py   # ya viene del esqueleto
│   ├── dominio/         # arranca: clase del ítem (Receta)
│   │   └── receta.py
│   ├── persistencia/
│   │   └── texto.py     # sin usar todavía (los .txt recién en E5)
│   └── tads/            # vacío por ahora (E3)
├── data/                    # queda disponible; se lee recién en E5
│   ├── recetas.txt
│   ├── ingredientes.txt
│   └── subrecetas.txt
└── docs/
    ├── INFORME.md
    └── DECLARACION_IA.md
```

En E1 puede andar con `list` de dicts de Python; no hace falta `ListaEnlazada` todavía.

## 5. Tag y regresión

```text
git add . && git commit -m "E1: repo y catálogo listo"
git tag entrega-1
git push && git push origin entrega-1
```

El código se corrige **sobre el tag**, no sobre un commit suelto de `main`. Todo lo que entre la próxima se corrige como regresión: no romper lo que ya funcionó.