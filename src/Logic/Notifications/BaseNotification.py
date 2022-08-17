
class BaseNotification:
    def encode(self, index, sal, timer, text):
        self.writeInt(index)
        self.writeBoolean(sal)
        self.writeInt(timer)
        self.writeString(text)