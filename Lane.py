from PyQt4 import QtGui
from JamSpace import LaneSettings
import pyaudio
import wave

class Lane(QtGui.QWidget):

    def __init__(self, name):

        # set member variables:
        self.settings = LaneSettings()

        self.changeName(name)

    def changeName(self, name):

        self.settings.changeName(name)

    #def initUI(self):