from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import qApp, QAction
from JamSpace.Views.MainView import MainView
from JamSpace.Models.MainModel import MainModel
from JamSpace.Models.LaneSpaceModel import LaneSpaceModel
from pydub import AudioSegment
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
        newId = self.laneSpaceModel.addLane()

        # instruct the lane space to retrieve it's lanes from the model (refresh it's list):
        self.mainWindow.laneSpace.getLanes()

        # connect the new lane signals to their slots:
        newLane = next((l for l in self.mainWindow.laneSpace.laneList if l.model.id == newId), None)
        newLane.recordEvent[int].connect(self.startRecording)

        # set the project path for the new lane model:
        newLane.model.setDirectory(self.model.projectPath)

        '''
        # connect the lane signals to their slots:
        for laneView in self.mainWindow.laneSpace.laneList:
            laneView.recordEvent[int].connect(self.startRecording)

        for laneModel in self.laneSpaceModel.laneList:
            laneModel.setDirectory(self.model.projectPath) # set the project path for each lane '''

    @pyqtSlot()
    def startPlaying(self):

        wavList = []
        path = self.model.projectPath + "/Clips/"
        laneAudio = AudioSegment.empty()

        # concatenate all the clips associated with each lane:

        for laneModel in self.laneSpaceModel.laneList:

            for i in range(1, laneModel.numClips+1):

                filePath = path + laneModel.name + "-" + str(i) + ".wav"

                try:
                    clip = AudioSegment.from_file(filePath, format="wav")
                    laneAudio += clip

                except Exception as e:
                    print("Unable to open wav file: " + str(e))
                    continue

            #add the concatenated lane audio to the list & empty the template for re-use:
            wavList.append(laneAudio)
            laneAudio = AudioSegment.empty()

        # pass the list of wavs to the startPlaying thread:
        self.laneSpaceModel.playThread.setAudioSegments(wavList)

        # set the startPlaying thread's output path:
        self.laneSpaceModel.playThread.setOutputFilePath(path)

        # run the startPlaying thread:
        self.laneSpaceModel.startPlaying()

    @pyqtSlot()
    def stopPlaying(self):

        self.laneSpaceModel.stopPlaying()

    @pyqtSlot(int)
    def startRecording(self, laneID):

        #extract the lane in question:
        lane = next((l for l in self.laneSpaceModel.laneList if l.id == laneID), None)

        if lane is None:
            print("Lane with id " + laneID + " doesn't exist")
        else:
            print('Recording on lane ' + str(laneID)) # DEBUG
            lane.startRecording()

            # increment the clip number:
            lane.setOutputFileName()

    def signalSlotConfig(self):

        # connect each lane's recordEvent signal to the record method:
        for lane in self.mainWindow.laneSpace.laneList:
            lane.recordEvent[int].connect(self.startRecording)

        # connect the MainView Buttons to their corresponding slots:
        self.mainWindow.controlBar.addLaneBtn.clicked.connect(self.addLane)
        self.mainWindow.controlBar.playBtn.clicked.connect(self.startPlaying)
        self.mainWindow.controlBar.stopBtn.clicked.connect(self.stopPlaying)

        # connect the menu bar actions to their slots:
        self.mainWindow.exitAction.triggered.connect(qApp.quit)

    def promptProjectDir(self):

        directory = ''

        # prompt user until they choose a directory:
        while directory == '':
            directory = self.mainWindow.showDirectoryDialog()


        self.model.projectPath = directory

        # create the project directory structure:
        self.createDirStructure(directory)

        # pass the directory to each lane model:
        for model in self.laneSpaceModel.laneList:

            model.setDirectory(self.model.projectPath)


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