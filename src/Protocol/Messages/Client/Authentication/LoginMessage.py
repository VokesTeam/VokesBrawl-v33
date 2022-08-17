from Protocol.Messages.Server.Authentication.LoginOkMessage import LoginOkMessage 
from Protocol.Messages.Server.Home.OwnHomeData import OwnHomeData

from DataStream.ByteStream import Reader
from Utilities.Helpers import Helpers

class LoginMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.ID = self.readLong()
        self.Token = self.readString()
        self.major = self.readInt()
        self.minor = self.readInt()
        self.build = self.readInt()

    def process(self):
            self.ID = Helpers.randomID(self)
            self.Token = Helpers.randomStringDigits(self)
            LoginOkMessage(self.client, self.player).send()
            OwnHomeData(self.client, self.player).send()