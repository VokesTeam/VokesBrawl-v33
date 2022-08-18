
class LogicClientAvatar:
    def encode(self):
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeString(self.player.name)  # Name
        self.writeByte(self.player.nameset)  # NameSetByUser
        self.writeInt(0)
        
        self.writeVInt(8)  # Commodity Array Count
        
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
        self.writeVInt(2)
        self.writeVInt(self.player.tutorialState)  # Tutorial State
        
        self.writeVInt(2)