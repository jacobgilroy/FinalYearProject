from JamSpace.LaneController import LaneController
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject
import sys

class MainController:

    def __init__(self):

        # set member variables:
        self.numLanes = 1
        laneController = LaneController(self.numLanes)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec_())