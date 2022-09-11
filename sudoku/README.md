# Sudoku

En este proyecto se pretende generar un sudoku que se juega en la terminal. Para ello existen dos archivos al momento que son [sudoku.py](/sudoku/sudoku.py) y [verifySudoku.py](/sudoku/verifySudoku.py)

## [Sudoku.py](/sudoku/sudoku.py)

Este script es el encargado de generar un tablero de sudoku, el algoritmo para ello se basa en el articulo: [Generador de Sudoku](https://www.academia.edu/40154909/Generador_de_Sudoku) por Cristian Alejandro Fandiño Mesa.

**Output**

![Sudoku Board](/img/sudoku_board.PNG "Sudoku Board")

## [verifySudoku.py](/sudoku/verifySudoku.py)

Este programa lo que hace es validar si un tablero está bien formado o no según las reglas del juego. El tablero se pasa como un string.

**LLamdo de funcion**

```py
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
```

**output**

~~~
YES
NO
~~~