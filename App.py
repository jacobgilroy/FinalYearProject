from JamSpace.MainController import MainController
import sys
import os
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':

    projPath = os.path.dirname(os.path.abspath(__file__))

    sys.path.insert(1, projPath)

    app = QApplication(sys.argv)
    mainController = MainController()
    sys.exit(app.exec_())