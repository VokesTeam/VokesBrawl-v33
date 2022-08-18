from DataStream.ByteStream import Reader
class EndClientTurnMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        pass

    def process(self):
        pass