from Logic.Notifications.BaseNotification import BaseNotification
class TicketCompensationNotification:
    def encode(self):
        self.writeVInt(74)
        BaseNotification.encode(self, 2, True, 0, '')
        self.writeVInt(0)
        self.writeVInt(0)