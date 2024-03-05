import misc

def wyznaczanie_pierwiastka(funkcja, xn, xn1):
    xn=float(xn)
    xn1=float(xn1)
    return xn - ((misc.horner(xn, funkcja, 3)*(xn-xn1))/(misc.horner(xn,funkcja,3)-misc.horner(xn1,funkcja,3)))

def metoda_siczenych(funkcja, x1, x2):
    f1 = misc.horner(float(x1), funkcja,  3)
    f2 = misc.horner(float(x2), funkcja, 3)

    while not misc.szacowanie_dokladnosci(float(x1), float(x2), 0.00000001):
        x3 = x2
        x2 = wyznaczanie_pierwiastka(funkcja, x2, x1)
        x1 = x3
    print(x2, " x2")
    print(misc.horner(x2, funkcja, 3))
        
