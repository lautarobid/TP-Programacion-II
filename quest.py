class Quest:
    def __init__(self, name: str, description: str, rewards:str, quest_complete:bool=False):
        self.__name = name
        self.__description = description
        self.__rewards = rewards
        self.__quest_complete = quest_complete

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description: str) -> None:
        self.__description = new_description

    @property
    def rewards(self) -> str:
        return self.__rewards

    @rewards.setter
    def rewards(self, new_rewards: str) -> None:
        self.__rewards = new_rewards

    def complete_quest(self):
        self.quest_complete = True

    def is_completed(self) -> bool:
        return self.quest_complete