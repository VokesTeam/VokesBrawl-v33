from Logic.Notifications.BaseNotification import BaseNotification

class ProLeagueSeasonEndNotification:
    def encode(self):
        self.writeVInt(77)
        BaseNotification.encode(self, 3, False, 0, '')
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)