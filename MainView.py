from PyQt5.QtWidgets import QWidget, QSplitter, QVBoxLayout, QFrame, QFileDialog
from PyQt5.QtCore import Qt
from JamSpace.Views.LaneSpaceView import LaneSpaceView
from JamSpace.Views.ControlBar import ControlBar

class MainView(QWidget):

    def __init__(self):

        super().__init__()

        # declare member variables:
        self.laneSpace = LaneSpaceView(parent=self)
        self.controlBar = ControlBar(parent=self)

        self.WIDTH = 900
        self.HEIGHT = 700

        # Initialise the UI:
        self.initUI()

    def initUI(self):

        self.setGeometry(20, 30, self.WIDTH, self.HEIGHT)
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

        vSplitter.addWidget(self.controlBar)
        vSplitter.addWidget(self.laneSpace)
        vSplitter.addWidget(hSplitter)

        vbox = QVBoxLayout(self)
        vbox.addWidget(vSplitter)

       #vbox.setAlignment(Qt.AlignTop)

        self.setLayout(vbox)

        self.show()

    def showDirectoryDialog(self):

        dirSelectionDialog = QFileDialog(self)

        projectDir = QFileDialog.getExistingDirectory(dirSelectionDialog, 'Select Project Folder')

        return projectDir