# def horner(x, wspolczynniki):
#     #TODO to może być źle
#     wynik = float(wspolczynniki[0])
#     for i in wspolczynniki[1:]:
#         wynik = float(i) + float((float(x) * float(wynik)))
#     return wynik

def horner(x, wsp):
    wynik = 0
    for i in wsp:
        wynik = wynik*x + i
    return wynik

def szacowanie_dokladnosci(b,a,e):
    if (abs(float(a)-float(b)) < e):
        return True
    else:
        return False

