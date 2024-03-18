import misc
import wykresy

def wyznaczanie_pierwiastka(xn, xn1, typ):
    xn = float(xn)
    xn1 = float(xn1)
    fn = misc.obliczanieWartosciFunkcji(xn, typ)
    fn1 = misc.obliczanieWartosciFunkcji(xn1, typ)
    
    if fn-fn1 == 0.0:
        return xn
    
    return xn - ((fn * (xn - xn1)) / (fn - fn1))

def oblicz(a, b, typ, warunek, war_stop):
    if misc.obliczanieWartosciFunkcji(a, typ) * misc.obliczanieWartosciFunkcji(b, typ) > 0:
        print(f'Zly przedzial, zatrzymanie obliczen')
        return
    if misc.pochodne(a,typ) == 0:
        print("pochodna rowna 0, zatrzymanie obliczen")
        return   
    x0 = wyznaczanie_pierwiastka(a,b, typ)
    x1 = a
    x2 = b
    i = 0

    if warunek == 1:
        while (i < war_stop) and (misc.obliczanieWartosciFunkcji(x0, typ) != 0.0):
            if misc.pochodne(x2,typ) == 0:
                print("pochodna rowna 0, zatrzymanie obliczen")
                return
            x0 = wyznaczanie_pierwiastka(x1,x2, typ)
            x2 = x1
            x1 = x0
            i += 1
    else:
        while (not misc.szacowanie_dokladnosci(x1, x2, war_stop)) and (misc.obliczanieWartosciFunkcji(x0, typ) != 0.0):
            if misc.pochodne(x2,typ) == 0:
                print("pochodna rowna 0, zatrzymanie obliczen")
                return
            x0 = wyznaczanie_pierwiastka(x1,x2, typ)
            x2 = x1
            x1 = x0
            i += 1

    print(f'x = {x0}, iteracji: {i}')
    wykresy.rysuj(x0, typ, a, b)


    
# *Sprawozdanie
# oblicz(0.6, 2, 1, 1, 20) 
# oblicz(0.6, 2, 1, 2, 0.001) 

# oblicz(-0.5, 0.7, 2, 1, 20)
# oblicz(-0.5, 0.7, 2, 2, 0.001)

# oblicz(-1, 2, 3, 1, 20) 
# oblicz(-1, 2, 3, 2, 0.001)
    
# oblicz(-0.5, 1, 4, 1, 20)
# oblicz(-0.5, 1, 4, 2, 0.001)
    

#! problemy
#1
# oblicz(0.5, 1.5, 1, 1, 20) 
#2
# oblicz(-0.9, 0.6, 2, 1, 20)
    
#??
#2
# oblicz(-0.8, 0.6, 2, 1, 20)
# oblicz(-0.8, 0.6, 2, 2, 0.001)

#x^2
# oblicz(-1, 1, 5, 1, 20)