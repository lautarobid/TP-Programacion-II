class Articulo:
    def __init__(self, nombre: str, tipo: str, poder_ataque: int, defensa: int, efecto: str):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__poder_ataque = poder_ataque
        self.__defensa = defensa
        self.__efecto = efecto

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre: str) -> None:
        self.__nombre = new_nombre

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, new_tipo: str) -> None:
        self.__tipo = new_tipo

    @property
    def poder_ataque(self) -> int:
        return self.__poder_ataque

    @poder_ataque.setter
    def poder_ataque(self, new_poder_ataque: int) -> None:
        self.__poder_ataque = new_poder_ataque

    @property
    def defensa(self) -> int:
        return self.__defensa

    @defensa.setter
    def defensa(self, new_defensa: int) -> None:
        self.__defensa = new_defensa

    @property
    def efecto(self) -> str:
        return self.__efecto

    @efecto.setter
    def efecto(self, new_efecto: str) -> None:
        self.__efecto = new_efecto

    def __str__(self) -> str:
        return (f'''
        Nombre: {self.nombre}
        Tipo: {self.tipo}
        Poder de Ataque: {self.poder_ataque}
        Defensa: {self.defensa}
        Efecto: {self.efecto}''')