
class LaneSettings:

    def __init__(self):

        # set member variable defaults:
        self.name = "Lane Default"
        self.volume = 10
        self.record = False
        self.activated = True

    def changeName(self, name):

        self.name = name

    def changeVolume(self, newVol):

        self.volume = newVol

    def activate(self):

        self.activated = True

    def deActivate(self):

        self.activated = False