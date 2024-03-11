import misc


def wyznaczanie_pierwiastka(xn, xn1, typ):
    xn = float(xn)
    xn1 = float(xn1)
    fn = misc.obliczanieWartosciFunkcji(xn, typ)
    fn1 = misc.obliczanieWartosciFunkcji(xn1, typ)
    return xn - ((fn * (xn - xn1)) / (fn - fn1))

def nowe_sieczne(a, b, typ):
    if misc.obliczanieWartosciFunkcji(a, typ) * misc.obliczanieWartosciFunkcji(b, typ) > 0:
        print(f'zly przedzial')
        return
    x0 = 0
    x1 = a
    x2 = b
    i = 100
    while i > 0 and not misc.szacowanie_dokladnosci(x1, x2, 0.000000001):
        x0 = wyznaczanie_pierwiastka(x1,x2, typ)
        x2 = x1
        x1 = x0
        i -= 1
    print(x0)