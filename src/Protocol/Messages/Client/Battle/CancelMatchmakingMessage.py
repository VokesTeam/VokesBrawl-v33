from DataStream.ByteStream import Reader
from Protocol.Messages.Server.Battle.MatchMakingCancelledMessage import MatchMakingCancelledMessage

class CancelMatchmakingMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        pass

    def process(self):
        MatchMakingCancelledMessage(self.client, self.player).send()