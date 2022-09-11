def verifDominio(email):
    dominioPub = {"Google" : "gmail", "Windows" : "hotmail", "Yahoo" : "yahoo"}
    if "@" in email:
        i = email.index("@")
        aComparar = email.lower()[i:]
        dominio = "Propio"
        for clave in dominioPub:
            if dominioPub[clave] in aComparar:
                dominio = clave
    else:
        dominio = "Correo no valido"
    return dominio

for i in range(5):
    correo = input("ingrese correo: ")
    dominio = verifDominio(correo)
    if dominio == "Propio":
        print("Felicitaciones tienes un dominio propio")
    elif dominio == "Correo no valido":
        print(dominio)
    else:
        print("Usas el dominio de " + dominio)
