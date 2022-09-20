year = int(input("Introduzca un año: "))

def bisiesto(year):
  if year >= 1582:
      if year%4 != 0:
          BoC = "Año común"
      elif year%100 != 0:
          BoC = "Año bisiesto"
      elif year%400 != 0:
          BoC = "Año común"
      else:
          BoC = "Año bisiesto"
  else:
      BoC = 'No dentro del periodo del calendario gregoriano'
  
  return BoC

print(bisiesto(year)) 