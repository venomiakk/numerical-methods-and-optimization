import numpy as np
import matplotlib.pyplot as plt


def rysuj(funkcja, a, b, integral=0):
    """
    @param typ: rodzaj funkcji: 1 - 5
    @param a: lewy przedzial
    @param b: prawy przedzial
    """
    a = float(a)
    b = float(b)
    x_values = np.arange(start=a if a < b else b,
                         stop=b+0.01 if b > a else a+0.01,
                         step=0.01)


    fig, ax = plt.subplots()
    ax.plot(x_values, funkcja(x_values), label="Funkcja interpolowana")
    if integral!=0:
        plt.fill_between(x_values, funkcja(x_values), alpha=0.3, where=[(x > a) and (x < b) for x in x_values])
    ax.set_title('Wykres funkcji')

    ax.grid(True)
    ax.axhline(0, color='red', linewidth=0.5)
    ax.axvline(0, color='red', linewidth=0.5)

    plt.show()
