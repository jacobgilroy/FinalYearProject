from PyQt5.QtWidgets import QWidget
from JamSpace.Views.LaneView import LaneView
from JamSpace.Models.LaneSpaceModel import LaneSpaceModel

class LaneSpaceView(QWidget):

    def __init__(self, parent):

        super().__init__(parent)

        # declare member variables:
        self.model = LaneSpaceModel()
        self.numLanes = 0
        self.laneList = []

        defaultLane = LaneView(parent=self, laneNum=0)
        self.laneList.append(defaultLane)

        self.laneSelected = 0

        self.initUI()

    def initUI(self):

        self.show()

        #self.getLanes() # load the lanes

    # retrieve lane info from the model:
    #def getLanes(self):

        # iterate through the model's list and load the data:
        #for lane in self.model.laneList:
            #self.laneList[lane['id']].id = lane['id']

    #def refresh(self):

     #   self.numLanes = self.model.

'''
    def addLane(self):

        self.numLanes += 1
        newLane = LaneView(parent=self, laneNum = self.numLanes)
        self.laneList.append(newLane)

    def removeLane(self, laneNum):

        self.numLanes -= 1
        self.laneList.pop(laneNum)
'''