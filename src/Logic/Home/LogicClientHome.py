from Logic.Home.Entry.LogicDailyData import LogicDailyData
from Logic.Home.Entry.LogicConfData import LogicConfData
from Logic.Notifications.NotificationFactory import NotificationFactory
class LogicClientHome:
    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)
        
        self.writeLong(0, 1)
        
        self.writeVInt(0) #notification factory
        
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
