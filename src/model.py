import numpy as np
import queue
import copy

class Piece:
    
    def __init__(self, volume):
        self.volume = np.array(volume)
        self.xSize = self.volume.shape[0]
        self.ySize = self.volume.shape[1]
        self.zSize = self.volume.shape[2]
        self.name = ""
        self.color = ""

    def get1D(self):
        returnString = ""
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    returnString += str(self.volume[x][y][z])
        return returnString
    
    #rotate 90 CCW around x axis passing through middle of cube
    def rotateX(self, numTimes):
        self.volume = np.rot90(self.volume, k=numTimes, axes=(1,2))

    #rotate 90 CCW around y axis passing through middle of cube
    def rotateY(self, numTimes):
        self.volume = np.rot90(self.volume, k=numTimes, axes=(2,0))

    #rotate 90 CCW around z axis passing through middle of cube
    def rotateZ(self, numTimes):
        self.volume = np.rot90(self.volume, k=numTimes, axes=(0,1))

    def translateX(self, distance):
        
        if distance < 0:
            if np.count_nonzero(self.volume[:abs(distance),:,:]) != 0:
                return False
        if distance > 0:
            if np.count_nonzero(self.volume[self.xSize-distance:,:,:]) != 0:
                return False
        
        self.volume = np.roll(self.volume, distance, 0)
        return True;

    def translateY(self, distance):
        if distance < 0:
            if np.count_nonzero(self.volume[:,:abs(distance),:]) != 0:
                return False
        if distance > 0:
            if np.count_nonzero(self.volume[:,self.ySize-distance:,:]) != 0:
                return False
        
        self.volume = np.roll(self.volume, distance, 1)
        return True;

    def translateZ(self, distance):
        if distance < 0:
            if np.count_nonzero(self.volume[:,:,:abs(distance)]) != 0:
                return False
        if distance > 0:
            if np.count_nonzero(self.volume[:,:,self.zSize-distance:]) != 0:
                return False
        
        self.volume = np.roll(self.volume, distance, 2)
        return True;

    def isPiece(self,x,y,z):
        return self.volume[x][y][z] == 1
        
    def __eq__(self, other):
        return np.array_equal(self.volume, other.volume) 
    def __ne__(self, other):
        return not np.array_equal(self.volume, other.volume)

    def permuteAction(self, num):
        if num == 0:
            self.rotateX(1)
            return True
        elif num == 1:
            self.rotateY(1)
            return True
        elif num == 2:
            self.rotateZ(1)
            return True
        elif num == 3:
            return self.translateX(1)
        elif num == 4:
            return self.translateY(1)
        elif num == 5:
            return self.translateZ(1)
        elif num == 6:
            return self.translateX(-1)
        elif num == 7:
            return self.translateY(-1)
        elif num == 8:
            return self.translateZ(-1)
        else:
            print("Error: Invalid permute action on " + name)
