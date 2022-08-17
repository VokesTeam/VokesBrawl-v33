from Logic.Entry.LogicGemOffer import LogicGemOffer 

class LogicShopData:
    def encode(self):
            self.writeVInt(1) #amount

            self.writeVInt(1) # ItemID
            self.writeVInt(1) # Ammount
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)  # [0 = Offer, 2 = Skins 3 = Star Shop]

            self.writeVInt(0)  # Cost
            self.writeVInt(0) # Timer

            self.writeVInt(1)
            self.writeVInt(100)
            self.writeVInt(0)  # is Offer Purchased

            self.writeBoolean(True)
            self.writeVInt(0)  # [0 = Normal, 1 = Daily Deals]
            self.writeBoolean(True)
            self.writeInt(0)