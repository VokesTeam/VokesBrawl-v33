from DataStream.ByteStream import Writer
from Logic.Entry.LogicBattlePlayerMap import LogicBattlePlayerMap

class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        self.writeVInt(1)
        self.writeBoolean(False)
        self.writeVInt(1)
        
        self.writeLong(0, 1)
        
        self.writeVInt(0)  # Timestamp
        self.writeBoolean(0) #2 boolean go br
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeDataReference(15, 7) #map id
        self.writeBoolean(0) #battle player map
        
        self.writeVInt(1)  # player entry arraychik
        self.writeUInt8(1)
        self.writeLong(0, 1) #player id
        self.writeDataReference(16, self.player.homeBrawler) #brawler
        self.writeDataReference(29, 0) #skin
        
        self.writeVInt(0) #??
        self.writeVInt(0) #??
        self.writeVInt(1) #??
        self.writeVInt(3) #player state
        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        #sub_5C4E08
        self.writeString(self.player.name)
        self.writeVInt(100)
        self.writeVInt(28000000 + self.player.profileIcon)
        self.writeVInt(43000000 + self.player.nameColor)
        self.writeVInt(0)
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0)  # array
        
        self.writeVInt(0)  # array
        
        self.writeVInt(0)  # array
        
        self.writeByte(0)
        self.writeByte(0)
        self.writeByte(6)