from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout
from PyQt5.QtCore import pyqtSignal

class ControlBar(QWidget):

    addLaneSignal = pyqtSignal()

    def __init__(self, parent):

        super().__init__(parent)

        self.addLaneBtn = QPushButton('Add Lane', self)
        self.playBtn = QPushButton('Play', self)
        self.stopBtn = QPushButton('Stop', self)

        self.initUI()

    def initUI(self):

        # set the size of the buttons based on its text:

        addLaneWidth = self.addLaneBtn.fontMetrics().boundingRect(self.addLaneBtn.text()).width()
        addLaneHeight = self.addLaneBtn.fontMetrics().boundingRect(self.addLaneBtn.text()).height()

        playWidth = self.playBtn.fontMetrics().boundingRect(self.playBtn.text()).width()
        playHeight = self.playBtn.fontMetrics().boundingRect(self.playBtn.text()).height()

        stopWidth = self.stopBtn.fontMetrics().boundingRect(self.stopBtn.text()).width()
        stopHeight = self.stopBtn.fontMetrics().boundingRect(self.stopBtn.text()).height()

        self.addLaneBtn.setFixedSize(addLaneWidth + 10, addLaneHeight + 10)
        self.playBtn.setFixedSize(playWidth + 10, playHeight + 10)
        self.stopBtn.setFixedSize(stopWidth + 10, stopHeight + 10)

        hbox = QHBoxLayout(self)

        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.stopBtn)
        hbox.addWidget(self.addLaneBtn)

        self.setLayout(hbox)

        #self.signalSlotInit()

        self.show()


    #def signalSlotInit(self):

        #self.addLaneBtn.clicked.connect(self.addLaneEvent)


    #def addLaneEvent(self):

        #self.addLaneSignal.emit()