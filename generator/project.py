import random
import string


class GeneratorProject:

    def __init__(self, app):
        self.app = app


    def random_string(self, prefix, maxlen):
        symbol = string.ascii_letters
        return prefix + "".join(random.choice(symbol) for i in range(random.randrange(maxlen)))