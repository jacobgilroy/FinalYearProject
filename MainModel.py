

class MainModel:

    def __init__(self):

        # Declare member variables:

        self.projectFile = None
        self.projectName = "New Project"
        self.projectPath = None
        self.configFileHandle = None

        self.volume = 50
        self.sampleRate = 1

    def setProjectPath(self, projPath):

        self.projectPath = projPath

    def setProjectName(self, name):

        self.projectName = name

    def setProjectFile(self, proj):

        self.projectFile = proj

    def setConfigFileHandle(self, confHandle):

        self.configFileHandle = confHandle