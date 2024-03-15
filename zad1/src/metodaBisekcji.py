import misc
import wykresy

def metodaBisekcji(a, b, typ, warunek, war_stop):
    
    eps = 0
    x1 = float(a)
    x2 = float(b)
    if ((misc.obliczanieWartosciFunkcji(x1,typ) * misc.obliczanieWartosciFunkcji(x2, typ)) > 0):
        print("Zly przedzial, zatrzymanie obliczen")
        return
    
    x3 = float((x1 + x2) / 2)
    x = misc.obliczanieWartosciFunkcji(x3, typ)
    i = 0
    if warunek == 1:    
        while (i < war_stop) and (misc.obliczanieWartosciFunkcji(x3, typ) != 0):
            i += 1
            if misc.obliczanieWartosciFunkcji(x3, typ) * misc.obliczanieWartosciFunkcji(x1, typ) < 0:
                x2 = x3
            else:
                x1 = x3
            x = misc.obliczanieWartosciFunkcji(x3, typ)
            x3 = float((x1 + x2) / 2)
            eps = abs(war_stop - x3)
    else:    
        while (not misc.szacowanie_dokladnosci(x1, x2, war_stop)) and (misc.obliczanieWartosciFunkcji(x3, typ) != 0):
            i += 1
            if misc.obliczanieWartosciFunkcji(x3, typ) * misc.obliczanieWartosciFunkcji(x1, typ) < 0:
                x2 = x3
            else:
                x1 = x3
            x = misc.obliczanieWartosciFunkcji(x3, typ)
            x3 = float((x1 + x2) / 2)
            eps = abs(war_stop - x3)
    
    print(f'x = {x3}, iteracji: {i}, dokladnosc: {eps}')
    wykresy.rysuj(x3, typ, a, b)

# *Sprawozdanie

# metodaBisekcji(-0.5, 0.5, 1, 1, 200)

# metodaBisekcji(0.5, 1.5, 2, 2, 0.00001)

# metodaBisekcji(-3, 3, 3, 1, 22)
    
# metodaBisekcji(0, 1, 4, 2, 0.00001)