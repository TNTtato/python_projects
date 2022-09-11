#This program generates a Sudoku board

def genInitialMatrix():
    Matrix = [[0 for j in range(9)] for i in range(9)]
    
    from random import sample
    Matrix[0] = sample(range(1, 9 + 1), 9)
    for i in range(1, 9):
        Matrix[i] = Matrix[i-1][3:] + Matrix[i - 1][:3]
        if i >= 3 and i < 6:
            Matrix[i] = Matrix[i - 3][1:] + Matrix[i - 3][:1]
        if i >= 6:
            Matrix[i] = Matrix[i - 6][2:] + Matrix[i - 6][:2]
    return Matrix
            
def changeRows(sudoku):
    from random import choice
    Matrix = [[0 for j in range(9)] for i in range(9)]
    k = 0
    for i in range(3):
        ik = i + k
        avRow = [0, 1, 2]
        tempC = choice(avRow)
        avRow.remove(tempC)
        Matrix[ik] = sudoku[ik + tempC]
        tempC = choice(avRow)
        avRow.remove(tempC)
        Matrix[ik + 1] = sudoku[ik + tempC]
        Matrix[ik + 2] = sudoku[ik + avRow[0]]
        k += 2
    return Matrix

def rowsToColumns(Matrix):
    MatrixT = []
    for j in range(9):
        tempCol = []
        for i in range(9):
            tempCol.append(Matrix[i][j])
        MatrixT.append(tempCol)
    return MatrixT

def changeColumns(Matrix):
    return rowsToColumns(changeRows(Matrix))
    
def mixHorizontalBlocks(Matrix):
    from random import choice
    mixHorM = [[0 for k in range(9)] for l in range(9)]
    k = 0
    av = [0, 3, 6]
    for i in range(3):
        ik = i + k
        tempCh = choice(av)
        mixHorM[ik] = Matrix[tempCh]
        mixHorM[ik + 1] = Matrix[tempCh + 1]
        mixHorM[ik + 2] = Matrix[tempCh + 2]
        av.remove(tempCh)
        k += 2
    return mixHorM
def genMatrix():
    seedMatrix = genInitialMatrix()
    mixedRows = changeRows(seedMatrix)
    mixedColumns = changeColumns(mixedRows)
    bloH = mixHorizontalBlocks(mixedColumns)
    bloV = rowsToColumns(mixHorizontalBlocks(bloH))
    Matrix = rowsToColumns(bloV)
    Matrix = changeRows(Matrix)
    return Matrix
genMatrix()

def drawBoard(Matrix):
    print()
    print("    1 2 3   4 5 6   7 8 9")
    print(" ","+", "-"*21, "+")
    k = 0
    for i in range(3):
        ik = i + k
        print(ik + 1,"|", " ".join(map(str, Matrix[ik][:3])), "|", " ".join(map(str, Matrix[ik][3:6])), "|", " ".join(map(str, Matrix[ik][6:])), "|")
        print(ik + 2,"|", " ".join(map(str, Matrix[ik + 1][:3])), "|", " ".join(map(str, Matrix[ik + 1][3:6])), "|", " ".join(map(str, Matrix[ik + 1][6:])), "|")
        print(ik + 3,"|", " ".join(map(str, Matrix[ik + 2][:3])), "|", " ".join(map(str, Matrix[ik + 2][3:6])), "|", " ".join(map(str, Matrix[ik + 2][6:])), "|")
        print(" ","+", "-"*21, "+")
        k += 2

drawBoard(genMatrix())

   
#print(' ', list(range(1,10)))
#    print(' ', ' | '*9)
#    for k in range(9):
#        print(k +1, Matrix[k])

#def userMove():
#    return [position, Number]

#def checkMove(positionNumber):

#def playGame():



