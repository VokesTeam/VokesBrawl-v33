from Logic.Notifications.BaseNotification import BaseNotification
class StarPointsMigrationNotification:
    def encode(self, showatlaunch, howMuch):
        self.writeVInt(80)
        BaseNotification.encode(self, 1, showatlaunch, 0, '')
        self.writeVInt(howMuch)