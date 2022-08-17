from Logic.Notifications.BaseNotification import BaseNotification

class ProLeagueSeasonEndNotification:
    def encode(self):
        self.writeVInt(77)
        BaseNotification.encode(self, 3, True, 0, '')
        self.writeVInt(0) #??
        self.writeVInt(93) #your points
        self.writeVInt(2500) #star reward
        self.writeVInt(1) #your ranking
        self.writeVInt(5000) #star reward