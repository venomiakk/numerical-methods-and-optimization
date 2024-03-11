import misc


def medotaBisekcji(a, b, typ):
    i = 0
    x1 = float(a)
    x2 = float(b)
    x3 = float((x1 + x2) / 2)
    x = misc.obliczanieWartosciFunkcji(x3, typ)
    while (x != 0 and not misc.szacowanie_dokladnosci(x1, x2, 0.00000000000000001)) and i < 1000:
        i += 1
        if misc.obliczanieWartosciFunkcji(x3, typ) * misc.obliczanieWartosciFunkcji(x1, typ) < 0:
            x2 = x3
        else:
            x1 = x3
        x = misc.obliczanieWartosciFunkcji(x3, typ)
        x3 = float((x1 + x2) / 2)
    print("wynik: ", i, " ", x3)
