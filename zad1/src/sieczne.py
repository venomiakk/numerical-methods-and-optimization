import misc

def wyznaczanie_pierwiastka(funkcja, xn, xn1):
    
    return xn - ((misc.horner(xn, funkcja,3)*(xn-xn1))/(misc.horner(xn,funkcja,3)-misc.horner(xn1,funkcja,3)))

def metoda_siczenych(funkcja, x1, x2, pochodna):
    f1 = misc.horner(x1, funkcja, 3)
    f2 = misc.horner(x2, funkcja,3)

    while not misc.szacowanie_dokladnosci(x1, x2):
        # TODO
        return 0
        
