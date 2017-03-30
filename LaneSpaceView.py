from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from JamSpace.Views.LaneView import LaneView
from JamSpace.Models.LaneSpaceModel import LaneSpaceModel

class LaneSpaceView(QWidget):

    def __init__(self, parent):

        super().__init__(parent)

        # declare member variables:
        self.model = LaneSpaceModel()
        self.laneList = []

        self.gridLayout = QGridLayout(self)

        '''
        defaultLane = LaneView(parent=self, laneNum=1)
        self.laneList.append(defaultLane)
        '''

        self.vboxLayout = QVBoxLayout(self)

        self.initUI()

    def initUI(self):

        self.getLanes() # load the lanes

        self.show()


    # this method retrieves lane models from the LaneSpaceModel and instantiates corresponding lane views:
    def getLanes(self):

        self.laneList = []

        for laneModel in self.model.laneList:

            laneView = LaneView(parent=self, laneModel=laneModel)
            self.laneList.append(laneView)

        self.positionLanes()


    # this method stacks the lanes vertically:
    def positionLanes(self):

        self.gridLayout = QGridLayout(self)

        i = 0

        for lane in self.laneList:

            self.gridLayout.addWidget(lane, i, 0)
            i += 1

        self.setLayout(self.gridLayout)

'''
        for i in range(len(self.laneList)):

            current = self.laneList[i]
            height = current.HEIGHT

            if i == 0:
                current.setGeometry(0, 0, self.width(), height)

            else:
                previous = self.laneList[i-1]

                xPos = previous.x
                yPos = previous.y - previous.height()

                current.setGeometry(xPos, yPos, self.width(), height)

'''

    #def refresh(self):