import numpy as np
from sympy import *
import misc


def lagrange(typ, xnodes):
    print('--------------------')
    x = symbols('x')

    ynodes = [misc.obliczanieWartosciFunkcji(i, typ) for i in xnodes]

    h = abs(xnodes[0] - xnodes[1])
    print(f'h: {h}')

    t = (x - xnodes[0]) / h
    print(f't: {t}')

    L = 0
    for i in range(len(ynodes)):
        numerator = 1
        denominator = 1
        for j in range(len(ynodes)):
            if i != j:
                numerator *= t - j
                denominator *= i - j
        L += ynodes[i] * (numerator / denominator)

    L = simplify(L)
    print("L: ")
    pretty_print(L)
    f = Lambda(x, L)

    points = np.linspace(xnodes[0], xnodes[-1], 100)
    dif = [abs(f(x) - misc.obliczanieWartosciFunkcji(x, typ)) for x in points]
    print(f'Najwieksza roznica: {np.max(dif):.2f} dla x = {points[dif.index(np.max(dif))]:.2f}')


    return f

