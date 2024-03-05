def horner(x, wspolczynniki, stopien):
    wynik = wspolczynniki[0]
    for i in wspolczynniki[1:]:
        wynik = i + (x * wynik)
    return wynik

def szacowanie_dokladnosci():
    return 0

