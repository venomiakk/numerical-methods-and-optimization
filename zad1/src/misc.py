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
    return float(war)


def szacowanie_dokladnosci(b, a, e):
    if (abs(float(a) - float(b)) < e):
        return True
    else:
        return False


def horner(x):
    wsp = [1.0, 3.0, -5.0, 1.0]
    wynik = float(wsp[0])
    for i in wsp[1:]:
        wynik = (float(wynik) * float(x)) + i
    return wynik


def sinus(x):
    # obliczanie wartosci funkcji 20sin(3x)
    return 20 * math.sin(math.radians(3 * x))


def wykldanicza(x):
    # wartosc funkcji (1/3)^x
    return (1/3)**x - 5


def zlozenie(x):
    return sinus(x) + horner(x) * wykldanicza(x)
