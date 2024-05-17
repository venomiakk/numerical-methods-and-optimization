def funkcja_kwadratowa(x):
    return x ** 2

def funkcja_wykonaj(f, x):
    return f(x)

# Wywołanie funkcji 'funkcja_wykonaj' z funkcją 'funkcja_kwadratowa' jako argumentem
wynik = funkcja_wykonaj(funkcja_kwadratowa, 5)
print(wynik)  # Wydrukuje: 25