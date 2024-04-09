import metodaBisekcji
import sieczne
import wykresy



def interface():
    print("Wybierz funkcje:\n1. Wielomian x^3 + 3x^2 - 5x + 1 \n2. Funkcja trygonometryczna 20sin(3x)\n3. Funkcja wykladnicza (1/3)^x - 5\n4. Funkcja zlozona 20sin(3((1/3)^x - 1))")
    y = input()
    y = int(y)
    if y == 1: wykresy.rysuj(0, y, -5, 3, 0)
    if y == 2: wykresy.rysuj(0, y, -3, 3, 0)
    if y == 3: wykresy.rysuj(0, y, -1, 1, 0)
    if y == 4: wykresy.rysuj(0, y, -3, 3, 0)
    # print("Wybierz metode:\n1. Metoda bisekcji \n2. Metoda siecznych")
    # x = input()
    print("Wybierz warunek zatrzymania:\n1. Ilosc iteracji\n2. Dokładność wyznaczania pierwiastka")
    z = input()
    z = int(z)
    if z == 2:
        print("Podaj dokladnosc: ")
    else:
        print("Podaj liczbe iteracji")
    e = input()
    e = float(e)
    # if int(x) == 1:
    #     print("Podaj przedzial \na:")
    #     a = input()
    #     print("b:")
    #     b = input()
    #     metodaBisekcji.metodaBisekcji(a, b, y, z, e)
    # if int(x) == 2:
    #     print("Podaj przedzial \na:")
    #     a = input()
    #     print("b:")
    #     b = input()
    #     sieczne.oblicz(a, b, y, z, e)
    print("Podaj przedzial \na:")
    a = input()
    print("b:")
    b = input()
    xb = metodaBisekcji.metodaBisekcji(a, b, y, z, e)
    xs = sieczne.oblicz(a, b, y, z, e)
    wykresy.rysuj(xb, y, a, b, xs, 1)



