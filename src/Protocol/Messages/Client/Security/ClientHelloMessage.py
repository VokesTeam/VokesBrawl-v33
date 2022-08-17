from Protocol.Messages.Server.Security.ServerHelloMessage import ServerHelloMessage

from DataStream.ByteStream import Reader


class ClientHelloMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        ServerHelloMessage(self.client, self.player).send()