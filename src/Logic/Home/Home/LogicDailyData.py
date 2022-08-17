from Logic.Home.Home.LogicShopData import LogicShopData
class LogicDailyData:
    def encode(self):
        self.writeVInt(0) #timestamp?
        self.writeVInt(0) #timestamp?
        self.writeVInt(self.player.trophies) #trophies
        self.writeVInt(self.player.highestTrophies) #highest trophies
        self.writeVInt(0) #??
        self.writeVInt(self.player.trophyRoad) #trophy road
        self.writeVInt(self.player.expPoints) #exp points?
        
        self.writeDataReference(28, self.player.profileIcon) # player icon
        self.writeDataReference(43, self.player.nameColor) # player name color
        
        self.writeVInt(0) # array
        self.writeVInt(0) # array
        self.writeVInt(0) # array
        self.writeVInt(0) # array
        self.writeVInt(0) # array
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(1000)
        self.writeVInt(10)
        self.writeVInt(20)
        self.writeVInt(30)
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0) # array
        
        self.writeBoolean(False) #3 boolean go brr
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0)
        #LogicShopData.encode(self)
        
        self.writeVInt(0) # adstatus array
        
        self.writeVInt(200)
        self.writeVInt(0)
        
        self.writeVInt(0) # array
        
        self.writeVInt(99999)
        self.writeVInt(0)
        
        self.writeDataReference(16, self.player.homeBrawler) # menu Brawler
        
        self.writeString("RU")
        self.writeString("VokesTeam")
        
        self.writeVInt(1) # intvalueentry
        self.writeInt(1)
        self.writeInt(0)
        
        self.writeVInt(1) # cooldownentry
        self.writeVInt(0)
        self.writeDataReference(16, 0)
        self.writeVInt(0)
        
        self.writeVInt(1) # brawlpass seasondata
        for x in range(1):
            self.writeVInt(4) #season
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(0) #bplevel?
            self.writeUInt8(2)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
        
        self.writeVInt(1) # proleagueseasondata maybe!
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeBoolean(True) # != 0
        self.writeVInt(0) # logicquests
        
        self.writeBoolean(True) # != 0
        self.writeVInt(0) # vanityitems
        
        self.writeBoolean(True) # != 0
        for x in range(11): #logicplayerrankedseasondata
            self.writeVInt(0) 
        self.writeVInt(1) #a1[14] array
        self.writeUInt8(2)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeBoolean(False)