from DataStream.ByteStream import Writer
from Logic.Entry.LogicBattlePlayerMap import LogicBattlePlayerMap

class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeInt(1)

        self.writeVInt(1557129593)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(15)
        self.writeVInt(7) # map ID
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # high id
        self.writeInt(1)  # low id
        self.writeVInt(16)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(99999)
        self.writeVInt(99999)
        self.writeVInt(1)
        self.writeVInt(3)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("Ida Tech") # player name
        self.writeVInt(100)
        self.writeVInt(28000000)
        self.writeVInt(43000000)
        self.writeVInt(23)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(6)