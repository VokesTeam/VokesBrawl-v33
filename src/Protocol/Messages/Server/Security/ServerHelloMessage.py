from DataStream.ByteStream import Writer

class ServerHelloMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20100
        self.player = player

    def encode(self):
        self.writeInt(24)
        for x in range(24):
            self.writeByte(1)