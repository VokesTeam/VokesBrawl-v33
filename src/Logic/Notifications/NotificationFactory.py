from Logic.Notifications.FloaterTextNotification import FloaterTextNotification
from Logic.Notifications.StarPointsMigrationNotification import StarPointsMigrationNotification
from Logic.Notifications.TicketCompensationNotification import TicketCompensationNotification
from Logic.Notifications.ProLeagueSeasonEndNotification import ProLeagueSeasonEndNotification

class NotificationFactory:
    def encode(self):
        self.writeVInt(4)
        FloaterTextNotification.encode(self, False, 'Made by VokesTeam')
        StarPointsMigrationNotification.encode(self, True, 0)
        TicketCompensationNotification.encode(self)
        ProLeagueSeasonEndNotification.encode(self)
        