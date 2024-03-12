import misc
import wykresy

def wyznaczanie_pierwiastka(xn, xn1, typ):
    xn = float(xn)
    xn1 = float(xn1)
    fn = misc.obliczanieWartosciFunkcji(xn, typ)
    fn1 = misc.obliczanieWartosciFunkcji(xn1, typ)
    return xn - ((fn * (xn - xn1)) / (fn - fn1))

def oblicz(a, b, typ, warunek, war_stop):
    if misc.obliczanieWartosciFunkcji(a, typ) * misc.obliczanieWartosciFunkcji(b, typ) > 0:
        print(f'Zly przedzial, zatrzymanie obliczen')
        return
    if misc.pochodne(a,typ) == 0:
        print("pochodna rowna 0, zatrzymanie obliczen")
        return   
    x0 = 0
    x1 = a
    x2 = b
    i = 0
    if warunek == 1:
        while i < war_stop:
            if misc.pochodne(x2,typ) == 0:
                print("pochodna rowna 0, zatrzymanie obliczen")
                return
            x0 = wyznaczanie_pierwiastka(x1,x2, typ)
            # TODO: sprawdzic czy nie zamienic x1 z x2 po wyznacznaniu pierwiastka
            x2 = x1
            x1 = x0
            i += 1
    else:
        while not misc.szacowanie_dokladnosci(x1, x2, war_stop):
            if misc.pochodne(x2,typ) == 0:
                print("pochodna rowna 0, zatrzymanie obliczen")
                return
            x0 = wyznaczanie_pierwiastka(x1,x2, typ)
            x2 = x1
            x1 = x0
            i += 1
    
    print(f'x = {x0:.6f}, iteracji: {i}')
    wykresy.rysuj(x0, typ, a, b)