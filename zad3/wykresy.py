import numpy as np
import matplotlib.pyplot as plt
import misc


def rysuj(typ, a, b, interpolacja=0, nodes=0, funkcja=0):
    """
    @param typ: rodzaj funkcji: 1 - 5
    @param a: lewy przedzial
    @param b: prawy przedzial
    @param interpolacja:
    @param nodes:
    @param funkcja:
    """
    a = float(a)
    b = float(b)
    x_values = np.arange(start=a if a < b else b,
                          stop=b if b > a else a,
                            step=0.01)

    #wartosci wielomianow interpolowanych
    y_values = []
    for i in x_values:
        y_values.append(misc.obliczanieWartosciFunkcji(i, typ))
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label="Funkcja interpolowana")

    ax.set_title('Wykres funkcji')
    if typ == 1: ax.set_title(f'Wykres funkcji (1/3)x + 2 ')
    elif typ == 2: ax.set_title(f'Wykres funkcji 2|x|')
    elif typ == 3: ax.set_title(f'Wykres funkcji 3x^3 + 2x^2 - 3x - 2')
    elif typ == 4: ax.set_title(f'Wykres funkcji 2sin(3x)')
    elif typ == 5: ax.set_title(f'Wykres funkcji 2|3x^2 + 2x^2 - 3x - 2|')

    #rysowanie wielomianu interpolacyjnego
    if interpolacja != 0:
        iy_values = []
        for i in x_values:
            iy_values.append(funkcja(i))
        ax.plot(x_values, iy_values, label="Funkcja interpolacyjna", linestyle="--")
        plt.legend()
        for i in nodes:
            ax.scatter(i, misc.obliczanieWartosciFunkcji(i, typ), color="green", s=20)
    
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    plt.show()
