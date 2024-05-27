import fileIO
import numpy as np
import funkcje
import legendre
import horner
import wykresy
import matplotlib.pyplot as plt



def transformTO11(x, a, b):
    return (((b - a) * x) + (b + a)) / 2

def transformToAB(x, a, b):
    return 0.5 * (b - a) * x + 0.5 * (b + a)

def wsp_approx(k, f, a, b, l_wezlow):
    """
    @param k: stopien wielomianu wynikowego (aproksymacji)
    @param f: funkcja aproksymowana
    @param a: przedzial a (powinno być zawsze -1?)
    @param b: przedzial n (powinno być zawsze 1?)
    @param l_wezlow: liczba wezlow do obliczania wartosci
    @return:
    """
    wsp = []
    w = np.array(fileIO.read(l_wezlow)[0])
    x = np.array(fileIO.read(l_wezlow)[1])

    t = transformToAB(x, a, b)
    wt = transformToAB(w, a, b)
    # print("wsp")


    for i in range(k, -1, -1):
        # integral = np.sum(w * f(t) * t)
        integral = np.sum(w * f(t) * horner.oblicz(legendre.coefficients(i), t))

        integral *= (((2 * i) + 1) / 2)
        wsp.append(integral)


    rysf(wsp, a, b, f, k)
    err = blad(f, wsp, l_wezlow, k, t)
    return wsp, err


def blad(f, awsp, l_wezlow, k, t):
    w = np.array(fileIO.read(l_wezlow)[0])
    x = np.array(fileIO.read(l_wezlow)[1])
    # integral = np.sum((w * (f(x) - wart_wiel(k, x, awsp))) ** 2)
    err = np.sum(w*(f(t) - wart_wiel(k, t, awsp)) ** 2)
    err = np.sqrt(err)

    return err


def wart_wiel(k, x, wsp):
    wartosc = 0
    wsp = wsp[::-1]
    for i in range(k + 1):
        wartosc += wsp[i] * horner.oblicz(legendre.coefficients(i), x)
    return wartosc


def rysf(wsp, a, b, f, k):
    a = float(a)
    b = float(b)
    x_values = np.arange(start=a if a < b else b,
                         stop=b if b > a else a,
                         step=0.01)
    y_values = []
    for i in x_values:
        y_values.append(wart_wiel(k, i, wsp))

    y_values2 = []
    for i in x_values:
        y_values2.append(f(i))
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values2, label="aprosymowana")
    ax.plot(x_values, y_values, label="aproksymacja", linestyle="--")
    plt.legend()
    ax.set_title(f"Stopien wielomianu: {k}")
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    plt.show()

