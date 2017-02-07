from JamSpace.LaneSettings import LaneSettings
from JamSpace.RecordThread import RecordThread
from JamSpace.PlayThread import PlayThread

class LaneModel(object):

    def __init__(self, laneNum):

        self.id = laneNum

        self.laneSettings = LaneSettings()
        self.recordThread = RecordThread(self.id)
        self.playThread = PlayThread()

    def record(self):

        try:
            self.recordThread.start()
        except IOError:
            print("! An error has occurred !")
            print("*cannot record*")
            return False

        return True

    def stopRecording(self):

        self.recordThread.recording = False

    def play(self):

        try:
            self.playThread.start()
        except IOError:
            print("! An error has occurred !")
            print("*cannot playback*")