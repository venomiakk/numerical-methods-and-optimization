import numpy as np
import fileIO
from scipy.special import roots_legendre



def gauss_legendre(f, a, b, n):
    """
    Przybliżenie całki oznaczonej ∫f(x)dx na przedziale [a, b) za pomocą kwadratury Gaussa-Legendre'a.

    :param f: Funkcja do całkowania
    :param a: Początek przedziału całkowania
    :param b: Koniec przedziału całkowania
    :param n: Liczba punktów Gaussa-Legendre'a
    :return: Przybliżona wartość całki
    """
    # Pobierz węzły i wagi dla n-punktowej kwadratury Gaussa-Legendre'a
    # x, w = roots_legendre(n)
    # print(type(x1))
    w = np.array(fileIO.read(n)[0])
    x = np.array(fileIO.read(n)[1])
    # print(type(x))
    # Przekształć węzły z przedziału [-1, 1] na [a, b)
    t = 0.5 * (x + 1) * (b - a) + a

    # Oblicz sumę ważoną wartości funkcji
    integral = 0.5 * (b - a) * np.sum(w * f(t))

    return integral


# Przykład użycia:
if __name__ == "__main__":
    # Funkcja do całkowania
    def f(x):
        return np.sin(x)


    # Przedział całkowania
    a = 0
    b = np.pi

    # Liczba punktów Gaussa-Legendre'a
    n = 2

    wynik = gauss_legendre(f, a, b, n)
    print(f"Przybliżona wartość całki wynosi: {wynik}")
