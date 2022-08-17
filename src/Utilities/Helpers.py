import string
import random

class Helpers:

    def randomStringDigits(self):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))

    def randomID(self):
        length = 9
        return int(''.join([str(random.randint(0, 10)) for _ in range(length)]))
