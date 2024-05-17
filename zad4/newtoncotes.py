import numpy as np
import funkcje


def simpson(f, a, b, n):
    """
    Przybliżenie całki oznaczonej ∫f(x)dx na przedziale [a, b] za pomocą wzoru Simpsona.

    :param f: Funkcja do całkowania
    :param a: Początek przedziału całkowania
    :param b: Koniec przedziału całkowania
    :param n: Liczba podprzedziałów (musi być parzysta)
    :return: Przybliżona wartość całki
    """
    if n % 2 != 0:
        raise ValueError("Liczba podprzedziałów n musi być parzysta.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = y[0] + y[-1]
    for i in range(1, n, 2):
        integral += 4 * y[i]
    for i in range(2, n - 1, 2):
        integral += 2 * y[i]

    integral *= h / 3
    return integral


def calc(funkcja, a, b, e):
    n = 2
    wynik = simpson(funkcja, a, b, n)
    dokladnosc_osiagnieta = False
    i = 0
    while not dokladnosc_osiagnieta:
        i += 1
        n *= 2
        nowy_wynik = simpson(funkcja, a, b, n)
        if abs(nowy_wynik - wynik) < e:
            dokladnosc_osiagnieta = True
        wynik = nowy_wynik

    print(f"Iteracje: {i}")
    print(f"Wynik: {wynik}")
    return wynik


# Przykład użycia:
if __name__ == "__main__":
    # Funkcja do całkowania

    # Przedział całkowania
    a = 0
    b = np.pi

    # Liczba podprzedziałów (musi być parzysta)
    n = 2

    wynik = calc(funkcje.sin, a, b, 0.1)
    print(f"Przybliżona wartość całki wynosi: {wynik}")
