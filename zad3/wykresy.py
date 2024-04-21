import numpy as np
import matplotlib.pyplot as plt
import misc


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
    y_values = []
    for i in x_values:
        y_values.append(misc.obliczanieWartosciFunkcji(i, typ))
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)

    ax.set_title('Wykres funkcji')
    if typ == 1: ax.set_title(f'Wykres funkcji (1/3)x + 2 ')
    if typ == 2: ax.set_title(f'Wykres funkcji 2|x|')
    if typ == 3: ax.set_title(f'Wykres funkcji 3x^2 + 2x^2 - 3x - 2')
    if typ == 4: ax.set_title(f'Wykres funkcji 2sin(3x)')
    
    ax.grid(True)
    ax.axhline(0, color='red', linewidth=1)
    ax.axvline(0, color='red', linewidth=1)
    plt.show()
