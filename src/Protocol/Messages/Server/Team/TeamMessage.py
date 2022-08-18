from DataStream.ByteStream import Writer
from Logic.Entry.LogicBattlePlayerMap import LogicBattlePlayerMap

class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        pass