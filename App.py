from JamSpace.MainController import MainController
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainController = MainController()
    sys.exit(app.exec_())