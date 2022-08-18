
class AdStatus:
    def encode(self):
        self.writeVInt(0) #count
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)