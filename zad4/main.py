import legendre
import newtoncotes
import funkcje
import sympy as sy

print(
    "Wybierz funkcję:\n"
    "1. Liniowa (1/3)x + 2 \n"
    "2. Wartość bezwzględna 2|x| \n"
    "3. Wielomian 3x^3 + 2x^2 - 3x - 2 \n"
    "4. Trygonometryczna 2sin(x)\n"
    "5. Zlozenie 2|3x^2 + 2x^2 - 3x - 2|\n"
    "6. (2/3)^(x-1)\n"
    "7. wielomian x^5")
funkcja = int(input())

print("Podaj przedzial:\n a: ")
a = float(input())
print("b: ")
b = float(input())

print("Podaj dokladnosc:\n e: ")
e = float(input())

if funkcja in [1, 2, 3, 4, 5, 6]:
    x = sy.Symbol("x")
    if funkcja == 1:
        war = sy.integrate(funkcje.liniowa(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.liniowa, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.liniowa, a, b, e)
    if funkcja == 2:
        war = sy.integrate(funkcje.wartosc_bezwzgledna(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.wartosc_bezwzgledna, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.wartosc_bezwzgledna, a, b, e)
    if funkcja == 3:
        war = sy.integrate(funkcje.wielomian(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.wielomian, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.wielomian, a, b, e)
    if funkcja == 4:
        war = sy.integrate(2*sy.sin(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.sin, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.sin, a, b, e)
    if funkcja == 5:
        war = sy.integrate(funkcje.zlozenie(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.zlozenie, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.zlozenie, a, b, e)
    if funkcja == 7:
        war = sy.integrate(funkcje.maks(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.maks, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.maks, a, b, e)
    if funkcja == 6:
        war = sy.integrate(funkcje.wykladnicza(x), (x, a, b))
        print("\nFaktyczna wartosc: " + str(war))
        print("\nGauss-Legendre: \n")
        for j in range(2, 6):
            legendre.gauss_legendre(funkcje.wykladnicza, a, b, j)
        print("Newton-Cotes (wzór Simpsona): \n")
        newtoncotes.calc(funkcje.wykladnicza, a, b, e)