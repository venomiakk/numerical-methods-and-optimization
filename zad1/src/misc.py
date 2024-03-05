def horner(x, wspolczynniki, stopien):
    wynik = float(wspolczynniki[0])
    for i in wspolczynniki[1:]:
        wynik = float(i) + float((float(x) * float(wynik)))
    return wynik

def szacowanie_dokladnosci(b,a,e):
    if (abs(a-b) < e):
        return True
    else:
        return False

