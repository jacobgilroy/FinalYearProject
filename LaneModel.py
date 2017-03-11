from JamSpace.RecordThread import RecordThread
from JamSpace.PlayThread import PlayThread

class LaneModel:

    def __init__(self, laneID):

        # declare member variables:
        self.id = laneID
        self.name = "Lane " + str(laneID)
        self.recordThread = RecordThread()
        self.playThread = PlayThread()
        self.clips = [] # a list to store each wav associated with this lane
        self.activated = True
        self.volume = 50.0
        self.outputDir = ""

    def setDirectory(self, path):

        self.outputDir = path
        self.recordThread.setOutputPath(path)

    def setName(self, newName):

        self.name = newName

    def toggleActive(self):

        if self.activated:
            self.activated = False
        else:
            self.activated = True

    def changeVolume(self, newVol):

        self.volume = newVol

    def startRecording(self):

        if self.recordThread.recording:
            self.stopRecording()
        else:

            try:
                self.recordThread.start()
            except IOError:
                print("! An IO error has occurred !")
                print("*cannot record*")
                return False

        return True

    def stopRecording(self):

        self.recordThread.recording = False

    def play(self):

        try:
            self.playThread.start()
        except IOError:
            print("! An IO error has occurred !")
            print("*cannot playback*")

