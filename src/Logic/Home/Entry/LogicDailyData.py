from Logic.Home.Entry.ForcedDrops import ForcedDrops
from Logic.Home.Entry.LogicOfferBundle import LogicOfferBundle
from Logic.Home.Entry.AdStatus import AdStatus

class LogicDailyData:
    def encode(self):
        self.writeVInt(0)  #timestamp
        self.writeVInt(0)  #timestamp too lol
        self.writeVInt(self.player.trophies)  #trophies
        self.writeVInt(self.player.highestTrophies)  #highest trophies
        
        self.writeVInt(0) #??
        self.writeVInt(self.player.trophyRoad)  # trophy road reward
        self.writeVInt(self.player.expPoints)  #exp points
        
        self.writeDataReference(28, self.player.profileIcon)  #player icon
        self.writeDataReference(43, self.player.nameColor)  #name color
        
        self.writeVInt(0)  # array
        self.writeVInt(0)  # array
        self.writeVInt(0)  # array
        self.writeVInt(0)  # array
        
        self.writeVInt(0) #leaderboard region: 0 global, 1 asia
        self.writeVInt(self.player.highestTrophies) #trophy road highest trophies
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(1000)
        self.writeVInt(10)
        self.writeVInt(20)
        self.writeVInt(30)
        
        ForcedDrops.encode(self)
        
        self.writeUInt8(4) #token doubler
        
        #tag states == 0 - new, 2 - seen
        self.writeVInt(0) #token doubler tag state
        self.writeVInt(0) #??
        self.writeVInt(0) #coin packs tag state
        self.writeVInt(0) #name change cost
        self.writeVInt(0) #next name change timer
    
        self.writeVInt(0)
        #LogicOfferBundle.encode(self)
        
        AdStatus.encode(self)
        
        self.writeVInt(200) #available tokens
        self.writeVInt(0) #time till new tokens
        
        self.writeVInt(0)  # array
        
        self.writeVInt(0) #??
        self.writeVInt(0) #??
        
        self.writeDataReference(16, self.player.homeBrawler)  # selected brawler
        
        self.writeString("RU")
        self.writeString("VokesTeam")  # content creator
        
        self.writeVInt(1) # intvalueentry
        self.writeLong(0, 0)
        
        self.writeVInt(1)  # cooldown entry
        self.writeVInt(0)
        self.writeDataReference(16, 0)
        self.writeVInt(0)
        
        self.writeVInt(1)  #brawl pass
        for x in range(1):
            self.writeVInt(4)
            self.writeVInt(0)
            self.writeByte(0)
            self.writeVInt(1)
            self.writeByte(0)
        
        self.writeVInt(0)  # proleague season data
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
        
        self.writeBoolean(True) #logic quests
        self.writeVInt(0)
        
        self.writeBoolean(True) #vanilniy items
        self.writeVInt(0)
        for x in range(0):
            self.writeDataReference(52, x)
            self.writeVInt(1)
            for x in range(1):
                self.writeVInt(1)
                self.writeVInt(1)