import json
from Logic.Entry.LogicBattlePlayerMap import LogicBattlePlayerMap

class LogicEventData:
    def encode(self):
        try:
            events = json.loads(open("src/Logic/JSONData/Events.json", 'r').read())
        except:
            events = json.loads(open("Logic/JSONData/Events.json", 'r').read()) #hehe
        self.writeVInt(16)
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 21, 22, 23, 24]:
            self.writeVInt(x)
        
        self.writeVInt(1)  # Events
        #Event Start
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeDataReference(15, 7)
        self.writeVInt(3)
        self.writeVInt(3)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1) #modifiers
        self.writeVInt(1)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeByte(0)
        self.writeVInt(0)
        
        self.writeVInt(0) # upcoming events array