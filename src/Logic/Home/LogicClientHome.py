from Logic.Home.Home.LogicDailyData import LogicDailyData
from Logic.Home.Home.LogicConfData import LogicConfData
class LogicClientHome:
    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)
        
        self.writeLong(0, 1)
        
        self.writeVInt(0) #notification factory array

        self.writeVInt(0)
        self.writeBoolean(False) # boolean


        self.writeVInt(0) # array
        self.writeVInt(0) # array