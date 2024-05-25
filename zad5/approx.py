import fileIO
import numpy as np
import funkcje
import legendre
import horner
import wykresy

def f1(x):
    return (3*x)-5

def f2(x):
    return horner.oblicz([3.0, 2.0, -3.0, -2.0], x)

def f3(x):
    return x**2

def transform(x, a, b):
    return ((2 * x) - a - b) / (b - a)
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
    # x = transform(x, a, b)
    x1 = transform(x, a, b)
    # print("wsp")

    for i in range(k, -1, -1):
        integral = np.sum(w * f(x) * horner.oblicz(legendre.coefficients(i), x))
        # print(integral)
        # integral = ((2*integral)-a-b) / (b-a)
        integral = (((2*i)+1)/2) * integral
        wsp.append(integral)
    # print(wsp)
    wykresy.poglad(wsp, a, b)
    # wykresy.poglad([3, -5], a, b)
    blad(f, wsp, l_wezlow)


def blad(f, fa, l_wezlow):
    w = np.array(fileIO.read(l_wezlow)[0])
    x = np.array(fileIO.read(l_wezlow)[1])
    integral = np.sum((w * (f(x) - horner.oblicz(fa, x)))**2)
    integral = np.sqrt(integral)
    print(integral)

if __name__ == "__main__":

    wsp_approx(5, f2, -1, 1, 4)

    # print("dsa")
    # for i in  range(2, 5):
    #     print(i)