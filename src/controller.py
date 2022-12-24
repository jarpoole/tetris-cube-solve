import queue
import copy
import datetime
from view import displayArray
from view import displayPieces
from model import Piece

class Controller:

    solutions = []
    
    def createPieces(self): #Z smallest, y next, x biggest
        puzzlePieces = []
        p1 = Piece([[[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p1.name = "Piece 1"
        p1.color = "yellow"
        

        p2 = Piece([[[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p2.name = "Piece 2"
        p2.color = "yellow"
        

        p3 = Piece([[[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
                    [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p3.name = "Piece 3"
        p3.color = "blue"
        

        p4 = Piece([[[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p4.name = "Piece 4"
        p4.color = "red"
       

        p5 = Piece([[[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p5.name = "Piece 5"
        p5.color = "blue"
        

        p6 = Piece([[[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p6.name = "Piece 6"
        p6.color = "yellow"
        

        p7 = Piece([[[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
                    [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p7.name = "Piece 7"
        p7.color = "red"
      

        p8 = Piece([[[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
                    [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p8.name = "Piece 8"
        p8.color = "red"
           

        p9 = Piece([[[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
                    [[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p9.name = "Piece 9"
        p9.color = "yellow"
        

        p10 = Piece([[[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p10.name = "Piece 10"
        p10.color = "red"
        

        p11 = Piece([[[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p11.name = "Piece 11"
        p11.color = "blue"
        

        p12 = Piece([[[1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]])
        p12.name = "Piece 12"
        p12.color = "blue"

        puzzlePieces.append(p8) #192
        puzzlePieces.append(p2) #216
        puzzlePieces.append(p3) #288
        puzzlePieces.append(p4) #288
        puzzlePieces.append(p5) #288
        puzzlePieces.append(p6) #288
        puzzlePieces.append(p7) #288
        puzzlePieces.append(p11)#288
        puzzlePieces.append(p9) #432
        puzzlePieces.append(p12)#432
        puzzlePieces.append(p1) #432
        puzzlePieces.append(p10)#648
        
        return puzzlePieces
        
    def permutePiece(self, piece):
        permuteQueue = queue.Queue()
        piecePermutes = []
        piecePermutes.append(piece)
        
        permuteQueue.put(piece)

        while not permuteQueue.empty():
            activePiece = permuteQueue.get()

            for i in range(9):
                newPiece = copy.deepcopy(activePiece)
                if newPiece.permuteAction(i) == True:
                    if newPiece not in piecePermutes:
                        piecePermutes.append(newPiece)
                        permuteQueue.put(newPiece)
        print("Found " + str(len(piecePermutes)) + " unique shape positions for " + piece.name + " within volume")
        return piecePermutes

    def export(self, pieces):
        f = open("permutations.txt", "w")
        for i in range(12): 
            f.write("#" + str(len(pieces[i])) + "\n")
            for permute in pieces[i]:
                f.write(permute.get1D() + "\n")
            
        f.close()

    def load(self, pieces):
        solutions = []
        
        f = open("solutions.txt", "r")
        solutionStrings = f.readlines()

        for solution in solutionStrings:
            solution = solution.strip(" ")
            if solution == '\n':
                continue
                
            solution = solution.replace("\n", "")
            solution = solution.strip(" ")
            solutionPieceChars = solution.split(" ")
          
            solutionPieceNumbers = [int(i) for i in solutionPieceChars]
            solutionPieces = []
            pieceNum = 0

            for solutionPieceNumber in solutionPieceNumbers:
                solutionPieces.append(pieces[pieceNum][solutionPieceNumber])
                pieceNum += 1
            solutions.append(solutionPieces)
        return solutions
                

    def run(self):
        print("Simulation started")
        currentDT = datetime.datetime.now()
        print("Start time: " + str(currentDT))
        
        #generate the pieces
        pieces = self.createPieces()
        for i in range(len(pieces)):
            pieces[i] = self.permutePiece(pieces[i])
        print(len(pieces))
        print(len(pieces[0]))

        #calculate the number of total combinations    
        combinations = 1
        for x in pieces:
            combinations *= len(x)
        print("Partial number of combinations to check is " + str(combinations))

        #Export
        if input("Would you like to export the permutations? y/n") == "y":
            self.export(pieces)

        #Load
        if input("Would you like to load the solutions? y/n") == "y":
            solutions = self.load(pieces)
            while(True):
                print("Press q to exit")
                solutionNum = input("Select a solution number [0 to " + str(len(solutions) - 1) + "]")
                if solutionNum == "q":
                    break
                else:
                    solutionNum = int(solutionNum)
                    for i in range(len(solutions[solutionNum]) + 1):
                        displayPieces(solutions[solutionNum][0:i])
            
        print("Simulation Complete")
        currentDT = datetime.datetime.now()
        print("End time: " + str(currentDT))

        for solution in Controller.solutions:
            displayPieces(solution.piecesUsed)
