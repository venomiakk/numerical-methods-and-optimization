import horner as h
import dokladnosc as d


def oblicz(wsp, a, b):
    if (h.oblicz(wsp, a) * h.oblicz(wsp, b)) > 0:
        print(f'Zły przedział')
        return

    x1 = float(a)
    x2 = float(b)
    i = 100
    x0 = 0
    while i > 0 and not d.oblicz(x1, x2, 0.000001):
        i -= 1
        x0 = (x1 + x2) / 2
        if h.oblicz(wsp, x0) == 0:
            return x0
        elif (h.oblicz(wsp, x0) * h.oblicz(wsp, x2)) < 0:
            x1 = x0
        else:
            x2 = x0

    return x0
