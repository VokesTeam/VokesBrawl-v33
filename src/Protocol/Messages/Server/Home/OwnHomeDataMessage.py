from DataStream.ByteStream import Writer
from Logic.Home.LogicClientHome import LogicClientHome
from Logic.Home.LogicClientAvatar import LogicClientAvatar


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)
        
        self.writeVInt(0)
        