from DataStream.ByteStream import Writer


class MatchMakingStatusMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20405
        self.player = player


    def encode(self):
        self.writeInt(0) # Matchmake Timer
        self.writeInt(1) # Current Players in Matchmake
        self.writeInt(6) # Maximum Players in Matchmake
        self.writeInt(1) # Play Again Accepted Players
        self.writeInt(0) # Play Again Maximum Players
        self.writeBoolean(False) # Matchmake Timer Enabled State