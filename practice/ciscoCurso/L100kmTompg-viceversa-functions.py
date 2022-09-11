#L/100km to mpg and viceversa
def l100kmtompg(liters):
    galons = liters / 3.785411784
    miles = 100 / 1.609344
    convertion = miles / galons
    return convertion


def mpgtol100km(miles):
    _100Km = miles * (1.609344 / 100)
    liters = 3.785411784
    convertion = liters / _100Km
    return convertion
print("\n\n\n")
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
