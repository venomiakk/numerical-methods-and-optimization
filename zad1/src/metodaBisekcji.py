import misc
import wykresy

def metodaBisekcji(a, b, typ, warunek, war_stop):
    
    x1 = float(a)
    x2 = float(b)
    if ((misc.obliczanieWartosciFunkcji(x1,typ) * misc.obliczanieWartosciFunkcji(x2, typ)) > 0):
        print("Zly przedzial, zatrzymanie obliczen")
        return
    
    x3 = float((x1 + x2) / 2)
    # x = misc.obliczanieWartosciFunkcji(x3, typ)
    i = 0
    if warunek == 1:    
        while (i < war_stop) and (misc.obliczanieWartosciFunkcji(x3, typ) != 0):
            i += 1
            if misc.obliczanieWartosciFunkcji(x3, typ) * misc.obliczanieWartosciFunkcji(x1, typ) < 0:
                x2 = x3
            else:
                x1 = x3

            # x = misc.obliczanieWartosciFunkcji(x3, typ)
            x3 = float((x1 + x2) / 2)

    else:    
        while (not misc.szacowanie_dokladnosci(x1, x2, war_stop)) and (misc.obliczanieWartosciFunkcji(x3, typ) != 0):
            i += 1
            if misc.obliczanieWartosciFunkcji(x3, typ) * misc.obliczanieWartosciFunkcji(x1, typ) < 0:
                x2 = x3
            else:
                x1 = x3

            # x = misc.obliczanieWartosciFunkcji(x3, typ)
            x3 = float((x1 + x2) / 2)
    
    print(f'x = {x3}, iteracji: {i}')
    wykresy.rysuj(x3, typ, a, b)


# *Sprawozdanie
# metodaBisekcji(0.6, 2, 1, 1, 20)
# metodaBisekcji(0.6, 2, 1, 2, 0.001)


# metodaBisekcji(-0.5, 0.7, 2, 1, 20)
# metodaBisekcji(-0.5, 1, 2, 2, 0.001)

# metodaBisekcji(-1, 2, 3, 1, 20)
# metodaBisekcji(-1, 2, 3, 2, 0.001)

# metodaBisekcji(-0.5, 1, 4, 1, 20)
# metodaBisekcji(-0.5, 1, 4, 2, 0.001)