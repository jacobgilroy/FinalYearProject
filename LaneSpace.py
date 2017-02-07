from PyQt5 import QtGui
from JamSpace import LaneView

class LaneSpace(QtGui.QWidget):

    def __init__(self):

        # initialise a sample lane:
        sampleLane = LaneView(name="Sample Lane")
        self.laneList = [sampleLane]

        self.cursorPosition = 0.0


    def createLane(self):

        # generate the name for the new lane:
        newPosition = len(self.laneList)
        newName = "Lane" + str(newPosition)

        newLane = LaneView(name=newName)

        self.laneList.append(newLane)

    def deleteLane(self, index):

        self.laneList.pop(index)

