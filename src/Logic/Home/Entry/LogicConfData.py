from Logic.Home.Entry.LogicEventData import LogicEventData
class LogicConfData:
    def encode(self):
        # sub_1B9CB8 start
        self.writeVInt(1) #beep

        LogicEventData.encode(self) #todo: complete this hsdfadskozoxckp
        
        self.writeLogicLongList([10, 20, 35, 75, 140, 290, 480, 800, 1250]) #writeArrayVInt
        self.writeLogicLongList([1, 2, 3, 4, 5, 10, 15, 20]) #writeArrayVInt
        self.writeLogicLongList([20, 50, 140, 280]) #writeArrayVInt
        self.writeLogicLongList([150, 400, 1200, 2600]) #writeArrayVInt
        
        self.writeBoolean(True)
        
        self.writeVInt(0) # release entry
        for x in range(0):
            self.writeDataReference(16, 0) #brawler (should be locked in gamefiles)
            self.writeInt(50) #countdown
        
        self.writeVInt(3) # intvalueentry

        self.writeLong(1, 41000021) # themeid
        self.writeLong(14, 1) # double token event
        self.writeLong(31, 0) # coin shower event
        
        self.writeVInt(2) # timedintvalue entry

        self.writeDataReference(14, 1)
        self.writeVInt(0)
        self.writeVInt(7325) #time left

        self.writeDataReference(31, 1)
        self.writeVInt(0)
        self.writeVInt(7325) # time left
        
        self.writeVInt(0) # customevent encode