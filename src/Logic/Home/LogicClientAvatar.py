
class LogicClientAvatar:
    def encode(self):
        for x in range(3):
            self.writeLogicLong(0, 1)
        
        self.writeString(self.player.name)
        self.writeBoolean(self.player.nameset) #nameset
        self.writeInt(0)
        
        self.writeVInt(8) # commodity count
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        #commodity end
        
        self.writeVInt(0) #gems
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2) #tutorial state