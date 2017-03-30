from JamSpace.Models.LaneModel import LaneModel
from JamSpace.PlayThread import PlayThread

class LaneSpaceModel:

    def __init__(self):

        # declare member variables:
        self.playThread = PlayThread()
        self.numLanes = 0
        self.laneSelected = 1
        self.laneList = [] # list of dictionaries to store each lane model

        self.addLane()  # add default lane

    def addLane(self):

        newID = self.numLanes + 1

        newLane = LaneModel(newID)
        self.laneList.append(newLane)
        self.numLanes += 1

    def removeLane(self, laneID):

        # remove the specified lane from the list:
        self.laneList[:] = [l for l in self.laneList if l.id != laneID]
        self.numLanes -= 1

    def getLaneList(self):

        return self.laneList

    def getNumLanes(self):

        return self.numLanes