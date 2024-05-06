import math


def obliczanieWartosciFunkcji(x, typ):
    war = 0.0
    typ = int(typ)
    # liniowa
    if typ == 1:
        war = horner(x, [1.0 / 3.0, 2.0])
    # wartosc bezwzgledna
    if typ == 2:
        war = modul(x)
    # wielomian
    if typ == 3:
        war = horner(x, [3.0, 2.0, -3.0, -2.0])
    # trygonometryczna
    if typ == 4:
        war = sinus(x)
    # zlozenie
    if typ == 5:
        war = zlozenie(x)
    if typ == 6:
        war = test(x)
    return float(war)


def x2(x):
    return x ** 2


def horner(x, wsp):
    # x^3 + 3x^2 - 5x + 1
    wynik = float(wsp[0])
    for i in wsp[1:]:
        wynik = (float(wynik) * float(x)) + i
    return wynik


def modul(x):
    return 2.0 * abs(x)


def sinus(x):
    # obliczanie wartosci funkcji 2sin(3x)
    return 2 * math.sin(3 * float(x))


def zlozenie(x):
    return modul(horner(x, [3.0, 2.0, -3.0, -2.0]))


def test(x):
    return abs(x*x*x)
