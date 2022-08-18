from Logic.Home.Entry.LogicDailyData import LogicDailyData
from Logic.Home.Entry.LogicConfData import LogicConfData
from Logic.Notifications.NotificationFactory import NotificationFactory
class LogicClientHome:
    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)
        
        self.writeLong(0, 1)
        
        NotificationFactory.encode(self)

        self.writeVInt(0)
        self.writeBoolean(False) # boolean

        self.writeVInt(0) # gatchadrop array
        for x in range(0):
            self.writeVInt(0)
            self.writeDataReference(0, 0)
            self.writeVInt(0)
            self.writeDataReference(0, 0)
            self.writeDataReference(0, 0)
            self.writeDataReference(0, 0)
            self.writeVInt(0)

        self.writeVInt(0) # array
        for x in range(0):
            self.writeDataReference(0, 0)