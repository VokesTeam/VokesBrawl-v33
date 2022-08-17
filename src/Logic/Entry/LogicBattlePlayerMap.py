class LogicBattlePlayerMap:
    def encode(self):
        self.writeByte(1) #writeBattlePlayerMap
        self.writeVInt(0) #Logic
        self.writeVInt(0) #Long
        self.writeString()
        self.writeVInt(0)
        
        self.writeVInt(0) #dataref
        
        self.writeInt(0) #CompressedString
        
        self.writeVInt(0) #Logic
        self.writeVInt(0) #Long
        
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0) #array
        #writeBattlePlayerMap end!