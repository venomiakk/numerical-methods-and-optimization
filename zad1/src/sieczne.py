import misc

def wyznaczanie_pierwiastka(funkcja, xn, xn1):
    xn=float(xn)
    xn1=float(xn1)
    return xn - ((misc.horner(xn, funkcja)*(xn-xn1))/(misc.horner(xn,funkcja)-misc.horner(xn1,funkcja)))

def metoda_siczenych(funkcja, x1, x2):
    f1 = misc.horner(float(x1), funkcja)
    f2 = misc.horner(float(x2), funkcja)

    while not misc.szacowanie_dokladnosci(float(x1), float(x2), 0.00000001):
        x3 = x2
        x2 = wyznaczanie_pierwiastka(funkcja, x2, x1)
        x1 = x3
    print(x2, " x2")
    print(misc.horner(x2, funkcja))
        
def nowe_sieczne(funkcja, x1, x2):
    #niby nowe ale dalaj działa tak samo...
    # result = float(0)
    f1 = misc.horner(x1, funkcja)
    f2 = misc.horner(x2, funkcja)
    i = 100
    while i > 0 and not misc.szacowanie_dokladnosci(x1,x2,0.000000001):
        # warunek |f1-f2| < ?
        x0 = wyznaczanie_pierwiastka(funkcja, x1, x2)
        print(x0)
        # if abs(misc.horner(funkcja, x0, 0)): #TODO poprawic ten warunek |f0| < e0 ??
        #     # return x0
        #     print(f'Otrzymany wynik: x = {x0}, y = {misc.horner(funkcja, x0, 0)}')
        x2 = x1
        x1 = x0
        f2 = f1
        f1 = misc.horner(x0, funkcja)
        i -= 1
        if i == 0:
            print(f'Przekroczono limit iteracji, uzyskany wynik: x = {x0}, y = {f1}' ) 
    # return x0
        print(f'Otrzymany wynik: x = {x0}, y = {f1}, po zaokrągleniu: x = {x0:.2f}, y = {misc.horner(x0, funkcja):.2f}')

nowe_sieczne([2,5,0], 1, 3)