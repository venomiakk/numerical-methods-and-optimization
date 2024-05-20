import legendre
import newtoncotes
import funkcje
import sympy as sy
import wykresy

print(
    "Wybierz funkcję:\n"
    "1. Liniowa (1/3)x + 2 \n"
    "2. Wartość bezwzględna 2|x| \n"
    "3. Wielomian 3x^3 + 2x^2 - 3x - 2 \n"
    "4. Trygonometryczna 2sin(x)\n"
    "5. Zlozenie 2|3x^2 + 2x^2 - 3x - 2|\n"
    "6. Wykladnicza (2/3)^(x-1)\n"
    "7. Wielomian x^6")
funkcja = int(input())

if funkcja == 1:
    wykresy.rysuj(funkcje.liniowa, -2, 2)
elif funkcja == 2:
    wykresy.rysuj(funkcje.wartosc_bezwzgledna, -2, 2)
elif funkcja == 3:
    wykresy.rysuj(funkcje.wielomian, -1.5, 1.5)
elif funkcja == 4:
    wykresy.rysuj(funkcje.sin, -4, 4)
elif funkcja == 5:
    wykresy.rysuj(funkcje.zlozenie, -1.5, 1.5)
elif funkcja == 6:
    wykresy.rysuj(funkcje.wykladnicza, -2, 8)
elif funkcja == 7:
    wykresy.rysuj(funkcje.maks, -0.2, 0.2)


print("Podaj przedzial:\n a: ")
a = float(input())
print("b: ")
b = float(input())

print("Podaj dokladnosc:\n e: ")
e = float(input())

if funkcja in [1, 2, 3, 4, 5, 6, 7]:
    x = sy.Symbol("x")
    if funkcja == 1:
        wykresy.rysuj(funkcje.liniowa, a, b, 1)
        war = sy.integrate(funkcje.liniowa(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.liniowa, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.liniowa, a, b, e)
    if funkcja == 2:
        wykresy.rysuj(funkcje.wartosc_bezwzgledna, a, b, 1)
        war = sy.integrate(funkcje.wartosc_bezwzgledna(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.wartosc_bezwzgledna, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.wartosc_bezwzgledna, a, b, e)
    if funkcja == 3:
        wykresy.rysuj(funkcje.wielomian, a, b, 1)
        war = sy.integrate(funkcje.wielomian(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.wielomian, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.wielomian, a, b, e)
    if funkcja == 4:
        wykresy.rysuj(funkcje.sin, a, b, 1)
        war = sy.integrate(2 * sy.sin(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.sin, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.sin, a, b, e)
    if funkcja == 5:
        wykresy.rysuj(funkcje.zlozenie, a, b, 1)
        war = sy.integrate(funkcje.zlozenie(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 51):
            legendre.gauss_legendre(funkcje.zlozenie, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.zlozenie, a, b, e)
    if funkcja == 7:
        wykresy.rysuj(funkcje.maks, a, b, 1)
        war = sy.integrate(funkcje.maks(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.maks, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.maks, a, b, e)
    if funkcja == 6:
        wykresy.rysuj(funkcje.wykladnicza, a, b, 1)
        war = sy.integrate(funkcje.wykladnicza(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.wykladnicza, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.wykladnicza, a, b, e)
