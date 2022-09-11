def isPalim(cadena):
    if cadena.lower() == cadena.lower()[::-1]:
        return "Es palindromo"
    else:
        return "No es palindromo"
print(isPalim("malayalam"))
