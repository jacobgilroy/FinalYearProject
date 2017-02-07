from PyQt5.QtWidgets import QMainWindow, QPushButton, QCheckBox, QLabel, QHBoxLayout, QVBoxLayout

class LaneView(QMainWindow):

    def __init__(self, laneNum):

        super().__init__()

        # set member variables:
        self.id = laneNum   # !! pass through the id from the main controller (list of lanes) !!
        self.name = "Lane " + str(laneNum)

        self.label = QLabel(self)
        self.label.setText(self.name)
        self.recBtn = QPushButton('Rec', self)
        self.activatedCb = QCheckBox("Activated", self)
        self.soloCb = QCheckBox("Solo", self)

        # temp button (should be in different place in gui):
        self.playBtn = QPushButton('Play', self)

        self.initUI()

    def initUI(self):

        # set the layout for the lane:

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

        self.show()

    def changeName(self, name):

        self.name = name