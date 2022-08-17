from Logic.Notifications.BaseNotification import BaseNotification

class FloaterTextNotification:
    def encode(self, showAtLaunch, text):
        self.writeVInt(66)
        BaseNotification.encode(self, 0, showAtLaunch, 0, text)