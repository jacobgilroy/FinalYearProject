from PyQt5.QtWidgets import QWidget, QPushButton, QCheckBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from JamSpace.Models.LaneModel import LaneModel

class LaneView(QWidget):

    # define event signals:
    recordEvent = pyqtSignal(int)

    def __init__(self, parent, laneNum):

        super().__init__(parent)

        # set member variables:
        self.id = laneNum   # pass through the id from the main controller (list of lanes)
        self.model = LaneModel(self.id)
        self.name = "Lane " + str(laneNum + 1)

        self.label = QLabel(self)
        self.label.setText(self.name)
        self.recBtn = QPushButton('Rec', self)
        self.activatedCb = QCheckBox("Activated", self)
        self.soloCb = QCheckBox("Solo", self)

        self.initUI()

    def initUI(self):

        # set the layout for the lane:

        # self.setGeometry(800, 100, 350, 80)
        hbox = QHBoxLayout(self)
        vboxLeft = QVBoxLayout(self)
        vboxRight = QVBoxLayout(self)

        vboxLeft.addWidget(self.label)
        vboxLeft.addWidget(self.recBtn)

        vboxRight.addWidget(self.soloCb)
        vboxRight.addWidget(self.activatedCb)

        hbox.addLayout(vboxLeft)
        hbox.addLayout(vboxRight)

        self.setLayout(hbox)

        self.signalSlotInit()

        self.show()

    def signalSlotInit(self):

        self.recBtn.clicked.connect(self.recordHandler)


    def changeName(self, name):

        self.name = name
        self.label.setText(name)
        self.model.changeName(name)

    def recordHandler(self):

        self.recordEvent.emit(self.id)

