def horner(x, wspolczynniki, stopien):
    wynik = wspolczynniki[0]
    for i in wspolczynniki[1:]:
        wynik = i + (x * wynik)
    return wynik

print(horner(0.432, [1,3,-5,1], 3))