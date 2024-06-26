import math


def obliczanieWartosciFunkcji(x, typ):
    war = 0
    typ = int(typ)
    if typ == 1:
        war = horner(x)
    if typ == 2:
        war = sinus(x)
    if typ == 3:
        war = wykldanicza(x)
    if typ == 4:
        war = zlozenie(x)
    if typ == 5:
        war = x2(x)
    return float(war)

def x2(x):
    return x**2

def szacowanie_dokladnosci(b, a, e):
    if (abs(float(a) - float(b)) < e):
        return True
    else:
        return False


def horner(x):
    # x^3 + 3x^2 - 5x + 1
    wsp = [1.0, 3.0, -5.0, 1.0]
    wynik = float(wsp[0])
    for i in wsp[1:]:
        wynik = (float(wynik) * float(x)) + i
    return wynik


def sinus(x):
    # obliczanie wartosci funkcji 20sin(3x)
    return 20 * math.sin(3 * float(x))


def wykldanicza(x):
    # wartosc funkcji (1/3)^x - 5
    return (1/3)**float(x) - 1.0


def zlozenie(x):
    return sinus(wykldanicza(x))

def pochodne(x, typ):
    typ = int(typ)
    if typ==1:
        wsp = [3, 6, -5.0]
        wynik = float(wsp[0])
        for i in wsp[1:]:
            wynik = (float(wynik) * float(x)) + i
        return wynik
    elif typ == 2:
        return 60*math.cos(math.radians(float(x)*3))
    elif typ == 3:
        return -3**(-float(x))*math.log(3)
    elif typ == 4:
        return -20 * 3**(1-float(x)) * math.cos((3*(3**(-float(x)) - 1))) * math.log(3)
    elif typ == 5:
        return 2*x
