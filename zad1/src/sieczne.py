import misc

def wyznaczanie_pierwiastka(funkcja, xn, xn1):
    
    return xn - ((misc.horner(xn, funkcja,3)*(xn-xn1))/(misc.horner(xn,funkcja,3)-misc.horner(xn1,funkcja,3)))

def metoda_siczenych(funkcja, a, b, pochodna):
    return 0
