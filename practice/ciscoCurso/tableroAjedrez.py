#Tablero de ajedrez
EMPTY = "-"
TORRE = "TORRE"
CABALLO = "CABALLO"
ALFIL = "ALFIL"
REY = "REY"
PEON = "PEON"
REINA = "REINA"
importantPieces = [TORRE, CABALLO, ALFIL, REINA, REY, ALFIL, CABALLO, TORRE]
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)
for i in range(8):
    tablero[1][i], tablero[6][i] = PEON, PEON
    tablero[0][i], tablero[7][i] = importantPieces[i], importantPieces[i]
print(tablero)
