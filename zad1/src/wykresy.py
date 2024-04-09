import numpy as np
import matplotlib.pyplot as plt
import misc


def rysuj(x, typ, a, b, d, c=0):
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
    if c != 0:
        ax.scatter(x, misc.obliczanieWartosciFunkcji(x, typ), color="green", label="metoda bisekcji", marker="v")
        ax.scatter(d, misc.obliczanieWartosciFunkcji(d, typ), color="violet", label="metoda siecznych", marker="+")
        plt.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.set_title('Wykres funkcji')
    if typ == 1: ax.set_title(f'Wykres funkcji x^3 + 3x^2 - 5x + 1')
    if typ == 2: ax.set_title(f'Wykres funkcji 20sin(3x)')
    if typ == 3: ax.set_title(f'Wykres funkcji (1/3)^x - 5')
    if typ == 4: ax.set_title(f'Wykres funkcji 20sin(3((1/3)^x - 1))')
    
    ax.grid(True)
    ax.axhline(0, color='red', linewidth=1)
    ax.axvline(0, color='red', linewidth=1)
    plt.show()
