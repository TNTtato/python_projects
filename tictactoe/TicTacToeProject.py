
def DisplayBoard(board):
    print("+-------"*3,"+", sep = "")
    for i in range(3):
        print("|       "*4)
        for j in range(3):
            print("|", str(board[i][j]) + "   ", sep = "   ", end = "")
        print("|")
        print("|       "*4)
        print("+-------"*3,"+", sep = "")
#
# la función acepta un parámetro el cual contiene el
#estado actual del tablero
# y lo muestra en la consola
#

def EnterMove(board):
    mov = int(input("\nIngrese movimiento: "))
    while True:
        if mov in board[0] or mov in board[1] or mov in board[2]:
            for i in range(3):
                for j in range(3):
                    if mov == board[i][j]:
                        board[i][j] = "O"
                        return board
        mov = int(input("Introduzca movimiento valido: "))                
#
# la función acepta el estado actual del tablero y pregunta
#al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la
#decisión del usuario
#

def MakeListOfFreeFields(board):
    listOfFreeFields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "O" and board[i][j] != "X":
                listOfFreeFields.append((i, j))
    return listOfFreeFields
#
# la función examina el tablero y construye una lista de
#todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par
#de números que indican la fila y columna
#
    

def VictoryFor(board, sign):
    emptyBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    threeXs = []
    threeOs = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                threeXs.append(emptyBoard[i][j])
            if board[i][j] == "O":
                threeOs.append(emptyBoard[i][j])
    winMatrix = [[1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [4, 5, 6], [7, 8, 9], [3, 5, 7]]
    contO = 0
    contX = 0
    for x in range(len(winMatrix)):
        for y in range(3):
            if winMatrix[x][y] in threeXs and len(threeXs) >= 3:
                contX +=1
        
            if winMatrix[x][y] in threeOs and len(threeOs) >= 3:
                contO += 1
                
        if contX == 3:
            return "Gana la máquina"
        else:
            contX = 0
        if contO == 3:
            return "Felicitaciones, ganaste"
        else:
            contO = 0
    if len(sign) == 0:
        return "Empate"
#
# la función analiza el estatus del tablero para verificar
#si
# el jugador que utiliza las 'O's o las 'X's ha ganado el
#juego
#

def DrawMove(board):
    from random import randrange
    mov = randrange(1, 10)
    while mov not in board[0] and mov not in board[1] and mov not in board[2]:
        mov = randrange(1, 10)
    for i in range(3):
        for j in range(3):
            if mov == board[i][j]:
                board[i][j] = "X"
    DisplayBoard(board)
    return board
#
# la función dibuja el movimiento de la maquina y
#actualiza el tablero
#
board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
DisplayBoard(board)
getOut = True
while getOut:
    board = EnterMove(board)
    DisplayBoard(board)
    listFree = MakeListOfFreeFields(board)
    win = VictoryFor(board, listFree)
    if win == "Felicitaciones, ganaste":
        print(win)
        getOut = False
    else:
        board = DrawMove(board)
        listFree = MakeListOfFreeFields(board)
        win = VictoryFor(board, listFree)
        if win != None:
            print(win)
            getOut = False

