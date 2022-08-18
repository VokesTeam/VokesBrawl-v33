from DataStream.ByteStream import Reader
from Protocol.Messages.Server.Team.TeamMessage import TeamMessage
from Protocol.Messages.Server.Team.TeamGameStartingMessage import TeamGameStartingMessage

class TeamSetMemberReadyMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        TeamGameStartingMessage(self.client, self.player).send()
        TeamMessage(self.client, self.player).send()