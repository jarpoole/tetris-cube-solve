class Cube:
    
    def __init__(self):
        x = 0
        y = 0
        z = 0

        xNext = None
        xPrev = None
        yNext = None
        yPrev = None
        zNext = None
        ZPrev = None

    def rotateX(self):   #Rotates along the x axis 
        temp = yNext
        yNext = zPrev
        zPrev = yPrev
        yPrev = zNext
        zNext = temp

        xNext.rotateX()
        xPrev.rotateX()
        yNext.rotateX()
        yPrev.rotateX()
        zNext.rotateX()
        zPrev.rotateX()

    def rotateY(self):   #Rotates along the y axis
        pass

    def rotateZ(self):   #Rotates along the z axis
        pass


class Model:

    puzzlePieces = []     

    def __init__(self):
        puzzleVolume = [][][]

    def createPieces(self):
        
        piece1 = Cube()
        piece1.xNext = Cube()
        piece1.xNext.yNext = Cube()
        piece1.xNext.zNext = Cube()
        piece1.xNext.xNext = Cube()
        puzzlePieces.append(piece1)
