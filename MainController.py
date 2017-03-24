from PyQt5.QtCore import pyqtSlot
from JamSpace.Views.MainView import MainView
from JamSpace.Models.MainModel import MainModel
from JamSpace.Models.LaneSpaceModel import LaneSpaceModel
import os

class MainController:

    def __init__(self):

        # Define member variables:
        self.mainWindow = MainView()
        self.model = MainModel()

        # obtain references to the Lane Space Model:
        self.laneSpaceModel = self.mainWindow.laneSpace.model

        self.signalSlotConfig()

        self.promptProjectDir()

    def addLane(self):

        # instruct the lanespace model to add a new lane:
        self.laneSpaceModel.addLane()

        # instruct the laneview to retrieve it's lanes from the model (refresh it's list):
        self.mainWindow.laneSpace.getLanes()

        # connect the new lane signals to their slots:
        for lane in self.mainWindow.laneSpace.laneList:
            lane.recordEvent[int].connect(self.startRecording)

    # method to refresh the GUI/views? *****

    '''    # this method refreshes laneModelList
    def getLaneModels(self):

        self.laneModelList = []

        for laneView in self.mainWindow.laneSpace.laneList:
            self.laneModelList.append(laneView.model)
    '''

    @pyqtSlot(int)
    def startRecording(self, laneID):

        #extract the lane in question:
        lane = next((l for l in self.laneSpaceModel.laneList if l.id == laneID), None)

        if lane is None:
            print("Lane with id " + laneID + " doesn't exist")
        else:
            print('Recording on lane ' + str(laneID)) # DEBUG
            lane.startRecording()

    def signalSlotConfig(self):

        # connect each lane's recordEvent signal to the record method:
        for lane in self.mainWindow.laneSpace.laneList:
            lane.recordEvent[int].connect(self.startRecording)

        # connect the MainView Buttons to their corresponding slots:
        self.mainWindow.controlBar.addLaneBtn.pressed.connect(self.addLane)

    def promptProjectDir(self):

        directory = ''

        # prompt user until they choose a directory:
        while directory == '':
            directory = self.mainWindow.showDirectoryDialog()


        self.model.projectPath = directory

        # create the project directory structure:
        self.createDirStructure(directory)

        # pass the directory to each lane model:

        clipsFolder = self.model.projectPath + "/Clips"
        for model in self.laneSpaceModel.laneList:

            model.setDirectory(clipsFolder)


    def createDirStructure(self, directory):

        projDir = directory + "/New Project"
        clipsFolder = projDir + "/Clips"

        # create project directory if it doesn't exist:
        try:
            if not os.path.exists(projDir):
                os.makedirs(projDir)
        except OSError as E:
            print(E)

        projectFilePath = projDir + "/" + self.model.projectName + ".jsf"
        configFilePath = projDir + "/" + "config.xml"

        # create project file if doesn't exist:
        try:
            projectFile = open(projectFilePath, 'r')
        except FileNotFoundError:
            projectFile = open(projectFilePath, 'w')

        projectFile.close()

        # create project config file if doesn't exist:
        try:
            configFileHandle = open(configFilePath, 'r')
        except FileNotFoundError:
            configFileHandle = open(configFilePath, 'w')

        configFileHandle.close()

        # create clips folder if doesn't exist:
        try:
            if not os.path.exists(clipsFolder):
                os.makedirs(clipsFolder)
        except OSError as E:
            print(E)

        # set the project info for the model:
        self.model.setProjectPath(projDir)
        self.model.setProjectFile(projectFile)
        self.model.setConfigFileHandle(configFileHandle)