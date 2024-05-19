import numpy as np
import fileIO
import funkcje



def gauss_legendre(f, a, b, n):
    w = np.array(fileIO.read(n)[0])
    x = np.array(fileIO.read(n)[1])

    t = ((a+b)/2) + (((b-a)/2) * x)

    integral = 0.5 * (b - a) * np.sum(w * f(t))

    print(f"Ilosc wezłów: {n}")
    print(f"Wynik: {integral}" + "\n")



if __name__ == "__main__":
    a = 0
    b = 3
    n = 5

    wynik = gauss_legendre(funkcje.zlozenie, a, b, n)

