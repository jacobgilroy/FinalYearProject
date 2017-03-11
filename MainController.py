from PyQt5.QtCore import pyqtSlot
from JamSpace.Views.MainView import MainView
from JamSpace.Models.MainModel import MainModel
from JamSpace.Models.LaneSpaceModel import LaneSpaceModel

class MainController:

    def __init__(self):

        # Define member variables:
        self.mainWindow = MainView()
        self.model = MainModel()

        # obtain references to the models:
        self.laneSpaceModel = self.mainWindow.laneSpace.model
        self.laneModelList = []
        self.getLaneModels()

        self.signalSlotConfig()

        self.getProjectDir()


    # method to refresh the GUI/views

    # this method refreshes laneModelList
    def getLaneModels(self):

        self.laneModelList = []

        for laneView in self.mainWindow.laneSpace.laneList:
            self.laneModelList.append(laneView.model)

    @pyqtSlot(int)
    def startRecording(self, laneID):

        #extract the lane in question:
        lane = next((l for l in self.laneModelList if l.id == laneID), None)

        if lane is None:
            print("Lane with id " + laneID + " doesn't exist")
        else:
            lane.startRecording()

    def signalSlotConfig(self):

        # connect each lane's recordEven signal to the record method:
        for lane in self.mainWindow.laneSpace.laneList:
            lane.recordEvent[int].connect(self.startRecording)


    def getProjectDir(self):

        directory = self.mainWindow.showDirectoryDialog()

        self.model.projectDirectory = directory

        for model in self.laneModelList:

            model.setDirectory(directory)