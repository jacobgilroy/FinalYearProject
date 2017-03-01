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


    # method to refresh the GUI/views

    # this method refreshes laneModelList
    def getLaneModels(self):

        self.laneModelList = []

        for laneView in self.mainWindow.laneSpace.laneList:
            self.laneModelList.append(laneView.model)

    def startRecording(self, laneID):

        lane = [l for l in self.laneModelList if l['id'] == laneID]
        lane.startRecording()

    def signalSlotConfig(self):

        # connect each lane's recordEven signal to the record method:
        for lane in self.mainWindow.laneSpace.laneList:
            lane.recordEvent.connect(self.startRecording)



