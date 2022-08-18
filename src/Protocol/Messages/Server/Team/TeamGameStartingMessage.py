from DataStream.ByteStream import Writer


class TeamGameStartingMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24130
        self.player = player

    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(23)
        self.writeVInt(0)