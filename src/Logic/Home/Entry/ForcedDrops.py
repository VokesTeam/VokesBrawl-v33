class ForcedDrops:
    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0) #array
        for x in range(0):
            self.writeVInt(0)