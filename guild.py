from personaje import Personaje

class Guild:
    def __init__(self, name: str, guild_master:Personaje):
        self.name = name
        self.members: List[Personaje] = []
        self.guild_master = guild_master
        self.guild_points = self.calculate_guild_points()

    def add_member(self, character: Personaje):
        self.members.append(character)
        self.guild_points = self.calculate_guild_points()

    def remove_member(self, character: Personaje):
        if character in self.members:
            self.members.remove(character)
            self.guild_points = self.calculate_guild_points()

    def calculate_guild_points(self) -> int:
        return sum(member.experience for member in self.members) + self.guild_master.experience

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def members(self) -> List[Personaje]:
        return self.__members

    @members.setter
    def members(self, new_members: List[Personaje]):
        self.__members = new_members

    @property
    def guild_master(self) -> Personaje:
        return self.__guild_master

    @guild_master.setter
    def guild_master(self, new_guild_master: Personaje):
        self.__guild_master = new_guild_master

    @property
    def guild_points(self) -> int:
        return self.__guild_points

    @guild_points.setter
    def guild_points(self, new_guild_points: int):
        self.__guild_points = new_guild_points