
class LogicConfData:
    def encode(self):
        # sub_1B9CB8 start
        self.writeVInt(1) #beep

        self.writeVInt(1)  # Count
        self.writeVInt(1)
        
        self.writeVInt(1) # eventdata array!
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(10)
        self.writeDataReference(15, 15)
        self.writeVInt(3)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0) #modifier array
        
        self.writeVInt(0)
        self.writeVInt(0)
        
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
        
        self.writeVInt(0) #writeArrayVInt
        self.writeVInt(0) #writeArrayVInt
        self.writeVInt(0) #writeArrayVInt
        self.writeVInt(0) #writeArrayVInt
        
        self.writeBoolean(False)
        
        self.writeVInt(0) # release entry
        
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
        self.writeVInt(700000) # time left
        
        self.writeVInt(0) # customevent encode