
class LogicClientAvatar:
    def encode(self):
        for x in range(3):
            self.writeLogicLong(0, 1)
        
        self.writeString(self.player.name)
        self.writeBoolean(self.player.nameset) #nameset
        self.writeInt(0)
        
        self.writeVInt(8) # commodity count
        
        # unlocked brawlers and resources array
        self.writeVInt(366)
        for x in range(362):
            self.writeDataReference(23, x)
            self.writeVInt(1)
        for x in [1, 8, 9, 10]:
            self.writeDataReference(5, x)
            self.writeVInt(99999)
        
         # brawlers trophies array
        self.writeVInt(46)
        for x in range(46):
            self.writeDataReference(16, x)
            self.writeVInt(1250)
        
         # brawlers trophies for rank array
        self.writeVInt(46)
        for x in range(46):
            self.writeDataReference(16, x)
            self.writeVInt(1250)
        
        # unknown array
        self.writeVInt(0)
        
         # brawlers powerpoints array
        self.writeVInt(46)
        for x in range(46):
            self.writeDataReference(16, x)
            self.writeVInt(1440)
        
         # brawlers power level array
        self.writeVInt(46)
        for x in range(46):
            self.writeDataReference(16, x)
            self.writeVInt(8)
        
         # starpowers and gadgets array
        self.writeVInt(386)
        for x in range(386):
            self.writeDataReference(23, x)
            self.writeVInt(1)
        
        # new brawler tag array
        self.writeVInt(0)
        #commodity end
        
        self.writeVInt(99999) # gems
        self.writeVInt(0) # free gems
        self.writeVInt(0) # player level
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2) #tutorial state