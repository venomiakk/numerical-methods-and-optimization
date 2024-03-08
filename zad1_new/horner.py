def oblicz(wsp, x):
    wynik = wsp[0]
    for i in wsp[1:]:
        wynik = (wynik * x) + i
    return wynik
