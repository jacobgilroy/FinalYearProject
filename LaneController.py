from JamSpace.Models.LaneModel import LaneModel
from JamSpace.Views.LaneView import LaneView
from PyQt5.QtWidgets import QApplication
import sys

class LaneController:

    def __init__(self, laneNum):


        #set member variables:
        self.model = LaneModel(laneNum)
        self.view = LaneView(laneNum)

        # initialise the lane UI:
        self.initUI()

    def initUI(self):

        # connect the UI signals to the correct slots:
        self.view.recBtn.clicked.connect(self.record)
        self.view.playBtn.clicked.connect(self.play)

    def record(self):

        success = self.model.record()

        if not success:
            print("!RECORDING FAILED!")

    def stopRecording(self):

        self.model.stopRecording()

    def play(self):

        self.model.play()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    controller = LaneController(1)
    sys.exit(app.exec_())