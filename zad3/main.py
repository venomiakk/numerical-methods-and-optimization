import wykresy
import interpolacja


def interface():
    print(
        "Wybierz funkcje:\n"
        "1. Liniowa (1/3)x + 2 \n"
        "2. Wartość bezwzględna 2|x| \n"
        "3. Wielomian 3x^3 + 2x^2 - 3x - 2 \n"
        "4. Trygonometryczna 2sin(3x)\n"
        "5. Zlozenie 2|3x^2 + 2x^2 - 3x - 2|")
    funkcja = int(input())

    if funkcja in [1, 2, 3, 4, 5]:
        wykresy.rysuj(funkcja, -1.5, 1.5)
    else:
        print("Niepoprawna funkcja")
        return -1

    print("Podaj przedzial:\n a: ")
    a = float(input())
    print("b: ")
    b = float(input())

    print("Podaj liczbe wezlow:")
    n = int(input())
    distance = abs(a - b) / float(n - 1)

    if 0 == distance:
        print("Niepoprawny przedzial")
        return -1

    xNodes = [a]
    for i in range(0, n - 1):
        xNodes.append(xNodes[i] + distance)

    f = interpolacja.lagrange(funkcja, xNodes)
    wykresy.rysuj(funkcja, a, b, 1, xNodes, f)
    return 0


if __name__ == '__main__':
    interface()


#TODO: obliczanie bledu
#TODO: czy blad ma byc dla wybranego punktu??
