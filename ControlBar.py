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

        hbox = QHBoxLayout(self)

        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.stopBtn)
        hbox.addWidget(self.addLaneBtn)

        self.setLayout(hbox)

#        self.signalSlotInit()

        self.show()


#    def signalSlotInit(self):

#        self.addLaneBtn.clicked.connect(self.addLaneEvent)


    def addLaneEvent(self):

        self.addLaneSignal.emit()