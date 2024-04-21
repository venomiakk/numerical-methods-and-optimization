import wykresy
from sympy import *
import misc

def interface():
    print(
        "Wybierz funkcje:\n"
        "1. Liniowa (1/3)x + 2 \n"
        "2. Wartość bezwzględna 2|x| \n"
        "3. Wielomian 3x^2 + 2x^2 - 3x - 2 \n"
        "4. Trygonometryczna 2sin(3x)\n"
        "5. Zlozenie 2|3x^2 + 2x^2 - 3x - 2|")
    funkcja = int(input())

    print("Podaj przedzial:\n a: ")
    a = input()
    print("b: ")
    b = input()

    if funkcja in [1, 2, 3, 4, 5]:
        wykresy.rysuj(funkcja, a, b)


def lagrange2():
    wenz = [[-1, 3], [0, 1], [1, 2], [2, -6]]


    x = symbols('x')
    n = len(wenz) - 1

    lambd_up = []
    lambd_down = []

    for i in range(len(wenz)):
        fup = 1
        fdown = 1
        for k in range(len(wenz)):
            if i != k:
                fup *= x - wenz[k][0]
                fdown = (wenz[i][0] - wenz[k][0]) * fdown

        lambd_up.append(fup)
        lambd_down.append(fdown)

    print(lambd_up)
    print(lambd_down)

    funk = 0
    for iter in range(len(wenz)):
        funk += wenz[iter][1] * (lambd_up[iter] / lambd_down[iter])

    print(funk)
    wyn = simplify(funk)
    pretty_print(wyn)
    f = Lambda(x, wyn)
    print(f(0))


def lagrange():
    # TODO: moga pojawiac sie dzielenia przez 0
    # TODO: funkcja interpolacyjna jest stopnia ilosc_wezlow - 1,
    # TODO: zatem trzeba cos zrobic z np. funkcja liniowa
    print("---------------------------------------")
    x = symbols('x')

    typ = 2
    xNodes = [0.0, 1.0, 2.0, 3.0]
    yNodes = [misc.obliczanieWartosciFunkcji(i, typ) for i in xNodes]
    print(yNodes)

    h = abs(xNodes[0] - xNodes[1])
    print(f'h: {h}')

    t = (x - xNodes[0]) / h
    tFun = Lambda(x, t)
    print(f't: {t, tFun(0)}')

    ans = []

    finalF = 0
    for a in range(len(yNodes)):
        print(a)
        tempF = 1
        for n in range(len(yNodes)):
            if a != n:
                tempF *= t - n
        print(f'rownanie: a{a}*{tempF}')

        tempEq = Lambda(x, tempF)
        an = yNodes[a]/tempEq(a)
        finalF += an * tempF
        print(f'y{a} = {yNodes[a]}, ^ rownanie({a}) = {tempEq(a)}, a{a} = {an}')

    print("wielomian interpolacyjny: ")
    print(finalF)
    simp = simplify(finalF)
    print(simp)
    # pretty_print(simp)
    return Lambda(x, finalF)

# print(h)
# lagrange2()
f = lagrange()
print(f(1))