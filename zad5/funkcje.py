import math
import horner


def obliczanieWartosciFunkcji(x, typ):
    war = 0.0
    typ = int(typ)
    # liniowa
    if typ == 1:
        war = horner.oblicz([1.0 / 3.0, 2.0], x)
    # wartosc bezwzgledna
    if typ == 2:
        war = modul(x)
    # wielomian
    if typ == 3:
        war = horner.oblicz([3.0, 2.0, -3.0, -2.0], x)
    # trygonometryczna
    if typ == 4:
        war = sinus(x)
    # zlozenie
    if typ == 5:
        war = zlozenie(x)
    if typ == 6:
        war = test(x)
    return float(war)


def linoiwa(x):
    return horner.oblicz([1.0 / 3.0, 2.0], x)

def x2(x):
    return x ** 2


def wielomian(x):
    return horner.oblicz([3.0, 2.0, -3.0, -2.0], x)

def modul(x):
    return abs(x)


def sinus(x):
    # obliczanie wartosci funkcji 2sin(3x)
    return 2 * math.sin(3 * float(x))


def zlozenie(x):
    return modul(horner.oblicz([3.0, 2.0, -3.0, -2.0], x))


def test(x):
    return (3*x) - 5
