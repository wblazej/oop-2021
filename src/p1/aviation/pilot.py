from airplane import Airplane

class Pilot:
    airplane: Airplane
    avaliable: bool

    def __init__(self, avaliable: bool = True):
        self.avaliable = avaliable
        self.airplane = None

    def __repr__(self):
        return f'| Airplane: {self.airplane}; Avaliable: {self.avaliable} |'