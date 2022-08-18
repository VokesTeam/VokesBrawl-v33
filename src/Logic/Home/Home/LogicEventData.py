import json
from Logic.Entry.LogicBattlePlayerMap import LogicBattlePlayerMap

class LogicEventData:
    def encode(self):
        try:
            events = json.loads(open("src/Logic/JSONData/Events.json", 'r').read())
        except:
            events = json.loads(open("Logic/JSONData/Events.json", 'r').read()) #hehe
        self.writeVInt(1)  # Count
        self.writeVInt(1)
        for event in events:
            self.writeVInt(1) # eventdata array!
            self.writeVInt(0)
            self.writeVInt(1)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeDataReference(15, event["ID"])
            self.writeVInt(3)
            self.writeVInt(0)
            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(1) #modifier array
            self.writeVInt(1)
        
            self.writeVInt(0)
            self.writeVInt(0)

            LogicBattlePlayerMap.encode(self)
        
            self.writeVInt(0)
        
            self.writeBoolean(True)
            self.writeVInt(0) #LogicRankedSeason
            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0) #array
            self.writeVInt(0) #array
            #Event end
        
        self.writeVInt(0) # events array