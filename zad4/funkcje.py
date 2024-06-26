import numpy as np


def sin(x):
    return 2 * np.sin(x)


def liniowa(x):
    return (1 / 3) * x + 2


def wartosc_bezwzgledna(x):
    return 2 * abs(x)


def wielomian(x):
    return 3 * x ** 3 + 2 * x ** 2 - 3 * x - 2


def zlozenie(x):
    return 2 * abs(3 * x ** 3 + 2 * x ** 2 - 3 * x - 2)

def maks(x):
    return x**6

def wykladnicza(x):
    return (2/3)**(x-1)
