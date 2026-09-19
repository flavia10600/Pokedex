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