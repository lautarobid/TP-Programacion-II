from personaje import Personaje
from habilidad import Habilidad

class Monstruos:
    def __init__(self, nombre: str, tipo: str, vida: int, ataque: int, defensa: int, velocidad: int):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa
        self.__velocidad = velocidad

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, new_tipo: str):
        self.__tipo = new_tipo

    @property
    def vida(self) -> int:
        return self.__vida

    @vida.setter
    def vida(self, new_vida: int):
        self.__vida = new_vida

    @property
    def ataque(self) -> int:
        return self.__ataque

    @ataque.setter
    def ataque(self, new_ataque: int):
        self.__ataque = new_ataque

    @property
    def defensa(self) -> int:
        return self.__defensa

    @defensa.setter
    def defensa(self, new_defensa: int):
        self.__defensa = new_defensa

    @property
    def velocidad(self) -> int:
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, new_velocidad: int):
        self.__velocidad = new_velocidad

    def atacar(self, personaje: Personaje) -> str:
        danio = self.ataque - personaje.agilidad
        if danio < 0:
            danio = 0
        personaje.vida -= danio
        if personaje.vida < 0:
            personaje.vida = 0
        mensaje_ataque = f"{self.nombre} atacó a {personaje.nombre} por {danio} de daño."
        mensaje_vida = f"La vida de {personaje.nombre} es de {personaje.vida}."
        return f"{mensaje_ataque}\n{mensaje_vida}"

    def recibir_ataque(self, personaje: Personaje) -> str:
        danio = personaje.fuerza - self.defensa
        if danio < 0:
            danio = 0
        self.vida -= danio
        if self.vida < 0:
            self.vida = 0
        return f"{personaje.nombre} atacó a {self.nombre} por {danio} de daño.\nLa vida de {self.nombre} es de {self.vida}"

    def recibir_habilidad(self, personaje: Personaje, habilidad: Habilidad) -> str:
        danio = habilidad.danio - self.defensa
        if danio < 0:
            danio = 0
        self.vida -= danio
        if self.vida < 0:
            self.vida = 0
        return f"{personaje.nombre} usó {habilidad.nombre} contra {self.nombre} causando {danio} de daño.\nLa vida de {self.nombre} es de {self.vida}"

    def pelea(self, personaje: Personaje, habilidad: Habilidad) -> str:
        vida_inicial = self.vida
        mensajes = []
        mensajes.append(f"Pelear contra {personaje.nombre}...")
        mensajes.append("----------------------------------------------")
        while self.vida > 0 and personaje.vida > 0:
            mensajes.append(self.recibir_habilidad(personaje, habilidad))
            if self.vida > 0:
                mensajes.append(self.atacar(personaje))
            mensajes.append("----------------------------------------------")
        if self.vida <= 0:
            mensajes.append(f"{self.nombre} ha sido derrotado.")
            self.vida = vida_inicial
        else:
            mensajes.append(f"{personaje.nombre} ha sido derrotado.")
        return "\n".join(mensajes)

    def __str__(self) -> str:
        return (f"Nombre: {self.nombre}\nTipo: {self.tipo}\nVida: {self.vida}\n"
                f"Ataque: {self.ataque}\nDefensa: {self.defensa}\nVelocidad: {self.velocidad}")

class Dragon(Monstruos):
    pass

class Orco(Monstruos):
    pass

class Arania(Monstruos):
    pass