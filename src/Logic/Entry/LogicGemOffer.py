
class LogicGemOffer:
    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeDataReference(0, 0)
        self.writeVInt(0)