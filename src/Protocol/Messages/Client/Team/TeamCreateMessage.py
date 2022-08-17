from DataStream.ByteStream import Reader
#from Protocol.Messages.Server.Team.TeamMessage import TeamMessage

class TeamCreateMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readBoolean()
        self.readUInt8()
        self.readLogicLong()
        self.readVInt()
        self.readDataReference()
        self.readLogicLong()

    def process(self):
        pass