

class LaneSpaceModel:

    def __init__(self):

        # declare member variables:
        self.numLanes = 1
        self.laneList = [] # list of dictionaries to store each lane's data

        self.addLane(laneID=0) # add default lane

    def addLane(self, laneID):

        newLane = {'id':laneID, 'volume':50}
        self.laneList.append(newLane)
        self.numLanes += 1

    def removeLane(self, laneID):

        # remove the specified lane from the list:
        self.laneList[:] = [l for l in self.laneList if l.get('id') != laneID]
        self.numLanes -= 1

    def getNumLanes(self):

        return self.numLanes