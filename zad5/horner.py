def oblicz(wsp, x):
    """
    @param wsp: wspolczynniki podawane od najwiekszego stopnia
    @param x: x
    @return: y w punkcie x
    """
    wynik = 0
    for i in wsp:
        wynik = wynik*x + i
    return wynik