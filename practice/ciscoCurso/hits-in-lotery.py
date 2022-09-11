#Encontrar numero de aciertos en una loteria
numbersPlayed = [5, 11, 9, 42, 3, 49]
winningNumbers = [3, 7, 11, 42, 34, 49]
hits = 0
for numb in numbersPlayed:
    if numb in winningNumbers:
        hits += 1

print(hits)
