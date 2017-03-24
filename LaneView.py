from PyQt5.QtWidgets import QWidget, QPushButton, QCheckBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from JamSpace.Models.LaneModel import LaneModel

class LaneView(QWidget):

    # define event signals:
    recordEvent = pyqtSignal(int)

    def __init__(self, parent, laneModel):

        super().__init__(parent)

        # set member variables:
        self.model = laneModel

        self.label = QLabel(self)
        self.recBtn = QPushButton('Rec', self)
        self.activatedCb = QCheckBox("Activated", self)
        self.soloCb = QCheckBox("Solo", self)

        self.HEIGHT = 80
        self.WIDTH = 150

        self.loadData()

        self.initUI()

    # this method loads data from the model:
    def loadData(self):

        self.label.setText(self.model.name)

    def initUI(self):

        # set the layout for the lane:

        #self.setGeometry(800, 100, 350, 80)

        self.setFixedHeight(self.HEIGHT)
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

    def setLabel(self, name):

        self.label.setText(name)

    def recordHandler(self):

        self.recordEvent.emit(self.model.id)

