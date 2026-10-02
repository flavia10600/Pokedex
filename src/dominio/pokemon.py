class Pokemon:
    # Esta clase esta basada en los atributos que se muestran en el csv de cada pokemon, esto fue creado con IA, me ayudo a crearlo mas rapido.
    def __init__(self, id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion):
        self.id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.nombre}\n"
            f"Tipo 1: {self.tipo1}\n"
            f"Tipo 2: {self.tipo2}\n"
            f"HP: {self.hp}\n"
            f"Ataque: {self.ataque}\n"
            f"Defensa: {self.defensa}\n"
            f"Velocidad: {self.velocidad}\n"
            f"Generación: {self.generacion}"
        )