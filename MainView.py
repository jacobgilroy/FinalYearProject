from PyQt5.QtWidgets import QWidget, QSplitter, QVBoxLayout, QFrame, QFileDialog, QScrollArea, QMenuBar, QAction, QToolBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from JamSpace.Views.LaneSpaceView import LaneSpaceView
from JamSpace.Views.ControlBar import ControlBar

class MainView(QWidget):

    def __init__(self):

        super().__init__()

        # declare member variables:
        self.laneSpace = LaneSpaceView(parent=self)
        self.controlBar = ControlBar(parent=self)
        self.menuBar = QMenuBar(self)
        self.toolBar = QToolBar(self)
        self.toolBar.show()

        self.laneScrollArea = QScrollArea()
        self.laneScrollArea.setWidgetResizable(True)

        self.WIDTH = 900
        self.HEIGHT = 700

        # Initialise the UI:
        self.initUI()

    def initUI(self):

        self.setGeometry(20, 30, self.WIDTH, self.HEIGHT)
        self.setWindowTitle('JamSpace')

        # configure the menu bar:

        # create menus:
        fileMenu = self.menuBar.addMenu('&File')
        editMenu = self.menuBar.addMenu('&Edit')

        # create actions:
        self.exitAction = QAction('Exit', self)
        self.exitAction.setStatusTip('Close the application')
        self.addLaneAction = QAction(QIcon('addLaneIcon.png'), 'Add Lane', self)
        self.playAction = QAction(QIcon('playIcon.png'), 'Play', self)
        self.stopAction = QAction(QIcon('stopIcon.ico'), 'Stop', self)

        self.addLaneAction.setStatusTip('Add a new lane')
        self.playAction.setStatusTip('Start playback')
        self.stopAction.setStatusTip('Stop playback')

        # add the actions to the menus/toolbar:
        fileMenu.addAction(self.exitAction)


        self.toolBar.addAction(self.playAction)
        self.toolBar.addAction(self.stopAction)
        self.toolBar.addAction(self.addLaneAction)

        self.laneScrollArea.setWidget(self.laneSpace)

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
        vSplitter.addWidget(self.laneScrollArea)
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