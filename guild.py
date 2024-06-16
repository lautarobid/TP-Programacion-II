from personaje import Personaje

class Guild:
    def __init__(self, name: str, guild_master:Personaje):
        self.name = name
        self.members: List[Character] = []
        self.guild_master = guild_master
        self.guild_points = self.calculate_guild_points()

    def add_member(self, character: Character):
        self.members.append(character)
        self.guild_points = self.calculate_guild_points()

    def remove_member(self, character: Character):
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
    def members(self) -> List[Character]:
        return self.__members

    @members.setter
    def members(self, new_members: List[Character]):
        self.__members = new_members

    @property
    def guild_master(self) -> Character:
        return self.__guild_master

    @guild_master.setter
    def guild_master(self, new_guild_master: Character):
        self.__guild_master = new_guild_master

    @property
    def guild_points(self) -> int:
        return self.__guild_points

    @guild_points.setter
    def guild_points(self, new_guild_points: int):
        self.__guild_points = new_guild_points