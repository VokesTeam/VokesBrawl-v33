from DataStream.ByteStream import Writer


class PlayerProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
        self.writeLogicLong(0, 1)
        self.writeVInt(0)

        self.writeVInt(45)
        for i in range(45):
            self.writeDataReference(16, i)
            self.writeDataReference(0, 0)
            self.writeVInt(1250)
            self.writeVInt(1250)
            self.writeVInt(10)

        self.writeVInt(15)

        self.writeVInt(1)
        self.writeVInt(0) # 3v3 victories

        self.writeVInt(2)
        self.writeVInt(self.player.expPoints) # exp

        self.writeVInt(3)
        self.writeVInt(self.player.trophies) # trophies

        self.writeVInt(4)
        self.writeVInt(self.player.highestTrophies) # highest trophies

        self.writeVInt(5)
        self.writeVInt(45)

        self.writeVInt(8)
        self.writeVInt(0) #solo victories

        self.writeVInt(11)
        self.writeVInt(0) # duo victories

        self.writeVInt(9)
        self.writeVInt(0) # rbr highest lvl

        self.writeVInt(12)
        self.writeVInt(0) # bg highest lvl

        self.writeVInt(13)
        self.writeVInt(0)

        self.writeVInt(14)
        self.writeVInt(0)

        self.writeVInt(15)
        self.writeVInt(0) # championship wins

        self.writeVInt(16)
        self.writeVInt(0) # rampage highest lvl

        self.writeVInt(17)
        self.writeVInt(0) # team league

        self.writeVInt(18)
        self.writeVInt(0) # solo league

        self.writeString(self.player.name)
        self.writeVInt(100)
        self.writeVInt(28000000 + self.player.profileIcon)
        self.writeVInt(43000000 + self.player.nameColor)

        self.writeBoolean(False)

        self.writeDataReference(0, 0)