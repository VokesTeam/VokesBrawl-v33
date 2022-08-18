import json
from Logic.Entry.LogicGemOffer import LogicGemOffer 

class LogicShopData:
    def encode(self):
        try:
            shop = json.loads(open("src/Logic/JSONData/Shop.json", 'r').read())
        except:
            shop = json.loads(open("src/Logic/JSONData/Shop.json", 'r').read())
        self.writeVInt(len(shop))
        for offer in shop:
            self.writeVInt(1)

            self.writeVInt(offer["ID"])
            self.writeVInt(offer["Ammount"])
            self.writeDataReference(16, offer["BrawlerID"])
            self.writeVInt(offer["SkinID"])
            self.writeVInt(offer["OfferType"])

            self.writeVInt(offer["Cost"])
            self.writeVInt(offer["Timer"])

            self.writeVInt(1)
            self.writeVInt(100)
            self.writeBoolean(offer["IsPurchased"])

            self.writeBoolean(False)
            self.writeVInt(offer["OfferDisplay"])
            self.writeBoolean(False)
            self.writeVInt(0)
            
            self.writeInt(0)
            self.writeString(offer["OfferText"])
            self.writeBoolean(False)
            self.writeString(offer["OfferBG"])
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(2)
            self.writeVInt(offer["Extra"]) # % Extra Text