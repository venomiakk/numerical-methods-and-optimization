import numpy as np
import matplotlib.pyplot as plt
import misc


def rysuj(x, typ, a, b):
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
    ax.scatter(x, misc.obliczanieWartosciFunkcji(x, typ), color="green", label="x0")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Wykres funkcji')
    
    ax.grid(True)
    ax.axhline(0, color='red', linewidth=1)
    ax.axvline(0, color='red', linewidth=1)
    plt.show()
