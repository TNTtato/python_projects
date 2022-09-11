#Verify a sudoku board

def convToList(arrSudoku):
    tempRow = ''
    sudoku = []
    for el in arrSudoku:
        if el.isdigit():
            tempRow += el
        else:
            sudoku.append(list(tempRow))
            tempRow = ''
    sudoku.append(list(tempRow))
    return sudoku

def verifyRows(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] in sudoku[i][:j]:
                return False
    return True

def tpSudoku(sudoku): #Transpose matrix
    sudokuT = []
    for j in range(9):
        tempCol = []
        for i in range(9):
            tempCol.append(sudoku[i][j])
        sudokuT.append(tempCol)
    return sudokuT

def verifyColumns(sudoku):
    tempSudo = tpSudoku(sudoku)
    return verifyRows(tempSudo)

def divInBlocks(sudoku):
    blockSudo = [[0 for j in range(9)] for i in range(9)]
    k = 0
    for i in range(3):
        ik = i + k
        blockSudo[ik] = sudoku[ik][:3] + sudoku[ik + 1][:3] + sudoku[ik + 2][:3]
        blockSudo[ik + 1] = sudoku[ik][3:6] + sudoku[ik + 1][3:6] + sudoku[ik + 2][3:6]
        blockSudo[ik + 2] = sudoku[ik][6:] + sudoku[ik + 1][6:] + sudoku[ik + 2][6:]
        k += 2
    return blockSudo

def verifyBlock(sudoku):
    return verifyRows(divInBlocks(sudoku))

def mainVerif(arrP):
    s = convToList(arrP)
    if verifyRows(s) and verifyColumns(s) and verifyBlock(s):
        print('YES')
    else:
        print('NO')

mainVerif("""295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672""")

mainVerif("""195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671""")
