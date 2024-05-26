import numpy as np
import matplotlib.pyplot as plt
import funkcje
import horner
import approx


def rysuj(typ, a, b):
    """
    @param typ: rodzaj funkcji: 1 - 5
    @param a: lewy przedzial
    @param b: prawy przedzial
    """
    a = float(a)
    b = float(b)
    x_values = np.arange(start=a if a < b else b,
                         stop=b if b > a else a,
                         step=0.01)

    # wartosci wielomianow interpolowanych
    y_values = []
    for i in x_values:
        y_values.append(funkcje.obliczanieWartosciFunkcji(i, typ))

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_values, y_values, label="Funkcja aproksymowana")

    ax.set_title('Wykres funkcji')
    if typ == 1:
        ax.set_title(f'Wykres funkcji (1/3)x + 2 ')
    elif typ == 2:
        ax.set_title(f'Wykres funkcji 2|x|')
    elif typ == 3:
        ax.set_title(f'Wykres funkcji 3x^3 + 2x^2 - 3x - 2')
    elif typ == 4:
        ax.set_title(f'Wykres funkcji 2sin(3x)')
    elif typ == 5:
        ax.set_title(f'Wykres funkcji 2|3x^2 + 2x^2 - 3x - 2|')

    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    plt.show()
    return fig


def rysuj_approx(awsp, k, a, b, f):
    a = float(a)
    b = float(b)
    x_values = np.arange(start=a if a < b else b,
                         stop=b if b > a else a,
                         step=0.01)
    y_values = []
    for i in x_values:
        y_values.append(approx.wart_wiel(k, i, awsp))

    y_values2 = []
    for i in x_values:
        if int == type(f):
            y_values2.append(funkcje.obliczanieWartosciFunkcji(i, f))
        else:
            y_values2.append(f(i))

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x_values, y_values2, label="funkcja aprosymowana")
    ax.plot(x_values, y_values, label="aproksymacja", linestyle="--")
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    plt.show()
    return fig
