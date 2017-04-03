from JamSpace.RecordThread import RecordThread
from JamSpace.PlayThread import PlayThread

class LaneModel:

    def __init__(self, laneID):

        # declare member variables:
        self.id = laneID
        self.name = "Lane " + str(laneID)
        self.recordThread = RecordThread()
        self.clips = [] # a list to store each wav associated with this lane
        self.numClips = 0
        self.activated = True
        self.volume = 50.0
        self.outputDir = ""
        self.outputFileName = ""

    def setDirectory(self, path):

        self.outputDir = path
        self.recordThread.setOutputPath(path)

        self.setOutputFileName()

    def setOutputFileName(self):

        # set the new output file name:
        self.outputFileName = self.name + "-" + str(self.numClips + 1)

        # set the record thread's output file name:
        self.recordThread.setOutputFileName(self.outputFileName)


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

        # call for the output file name to be updated:
        self.setOutputFileName()

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

        self.numClips += 1

        # update the output file name:
        self.setOutputFileName()