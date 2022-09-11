controlCicle = True
while controlCicle:
    try:
        x = int(input("Ingrese numero: "))
        y = 1 / x
        print(y)
        controlCicle = False
    except ZeroDivisionError:
        print("No puedes dividir entre cero")
    except ValueError:
        print("Solo entra numeros enteros")
    except:
        print("Algo ha salido mal o se interrumpio")

print("*----------------*", "END", "*----------------*", sep = "\n")
