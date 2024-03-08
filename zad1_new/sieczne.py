import horner as h
import dokladnosc as d


def pierwiastek(wsp, xn_1, xn):
    return xn - ((h.oblicz(wsp, xn) * (xn - xn_1)) / (h.oblicz(wsp, xn) - h.oblicz(wsp, xn_1)))


def oblicz(wsp, a, b):
    if (h.oblicz(wsp, a) * h.oblicz(wsp, b)) > 0:
        print(f'Zły przedział')
        return
    i = 100
    x0 = 0
    x1 = a
    x2 = b
    while i > 0 and not d.oblicz(x1, x2, 0.0001):
        x0 = pierwiastek(wsp, x1, x2)
        x2 = x1
        x1 = x0
        i -= 1

    return x0
