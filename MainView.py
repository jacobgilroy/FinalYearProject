from PyQt5.QtWidgets import QWidget, QSplitter, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
from JamSpace.Views.LaneSpaceView import LaneSpaceView

class MainView(QWidget):

    def __init__(self):

        super().__init__()

        # declare member variables:
        self.laneSpace = LaneSpaceView(parent=self)

        # Initialise the UI:
        self.initUI()

    def initUI(self):

        self.setGeometry(30,30, 900, 700)
        self.setWindowTitle('JamSpace')

        # Instantiate UI components:
        laneEditSpace = QFrame(self)
        laneEditSpace.setFrameShape(QFrame.StyledPanel)
        clipEditSpace = QFrame(self)
        clipEditSpace.setFrameShape(QFrame.StyledPanel)

        # Apply layout:
        vSplitter = QSplitter(Qt.Vertical)
        hSplitter = QSplitter(Qt.Horizontal)

        hSplitter.addWidget(laneEditSpace)
        hSplitter.addWidget(clipEditSpace)

        vSplitter.addWidget(self.laneSpace)
        vSplitter.addWidget(hSplitter)

        hbox = QHBoxLayout(self)
        hbox.addWidget(vSplitter)

        self.setLayout(hbox)

        self.show()