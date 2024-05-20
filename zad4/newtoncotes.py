import numpy as np
import funkcje


def simpson(f, a, b, n):
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
    i = 1
    while not dokladnosc_osiagnieta:
        i += 1
        n *= 2
        nowy_wynik = simpson(funkcja, a, b, n)
        if abs(nowy_wynik - wynik) < e:
            dokladnosc_osiagnieta = True
        wynik = nowy_wynik

    print(f"Iteracje: {i}")
    print(f'Ilość podprzedziałów: {n}')
    print(f'Dokładność: {e}')
    print(f"Wynik: {wynik}"+"\n")


if __name__ == "__main__":
    a = 0
    b = np.pi

    n = 3

    wynik = calc(funkcje.sin, a, b, 0.1)

