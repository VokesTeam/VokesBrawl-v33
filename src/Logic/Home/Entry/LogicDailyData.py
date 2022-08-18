from Logic.Home.Entry.ForcedDrops import ForcedDrops
from Logic.Home.Entry.LogicOfferBundle import LogicOfferBundle
from Logic.Home.Entry.AdStatus import AdStatus

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

        self.writeVInt(279) # array
        for x in range(279):
            self.writeDataReference(29, x)

        self.writeVInt(0) # array
        self.writeVInt(0) # array
        
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
        
        self.writeVInt(2) #token doubler tag state - 0 new 2 - seen
        self.writeVInt(0) #??
        self.writeVInt(2) #coin packs tag state - 0 new 2 - seen
        self.writeVInt(0) #name change cost
        self.writeVInt(0) #next name change timer
        
        
        LogicOfferBundle.encode(self)
        
        AdStatus.encode(self)
        
        self.writeVInt(200) #available tokens from battle
        self.writeVInt(0) #time till new tokens
        
        self.writeVInt(0) # array
        
        self.writeVInt(0) #?? 
        self.writeVInt(0) #??
        
        self.writeDataReference(16, self.player.homeBrawler) # menu Brawler
        
        self.writeString("RU")
        self.writeString("VokesTeam")
        
        self.writeVInt(6) # intvalueentry
        self.writeLong(3, 0) #token anim
        self.writeLong(4, 0) #trophies anim
        self.writeLong(10, 0) #pp anim
        self.writeLong(15, 0) #agescreen anim
        self.writeLong(18, 1) #esport button
        self.writeLong(20, 0) #gems anim
        
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
        
        self.writeVInt(0) # proleagueseasondata maybe!
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
        
        self.writeBoolean(True) # != 0
        self.writeVInt(0) # logicquests array

        
        self.writeBoolean(True) # != 0
        self.writeVInt(413) # vanityitems
        for x in range(413):
            self.writeDataReference(52, x)
            self.writeVInt(1)
            for x in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        self.writeBoolean(True) # != 0
        for x in range(11): #logicplayerrankedseasondata
            self.writeVInt(0) 
        self.writeVInt(1) #a1[14] array
        self.writeUInt8(2)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeBoolean(False)