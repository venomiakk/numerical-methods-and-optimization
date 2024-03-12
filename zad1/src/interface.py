import metodaBisekcji
import sieczne
def interface():
    print("1.wielomian \n2.funkcja trygonometryczna\n3.funkcja wykladnicza\n4.funkcja zlozona")
    y = input()
    print("1.Metoda bisekcji \n2.Metoda siecznych")
    x = input()
    print("Warunek zatrzymania:\n1. Ilosc iteracji\n2. Dokładność wyznaczania pierwiastka")
    z = input()
    z = int(z)
    if z==2 :
        print("Podaj dokladnosc: ")
    else:
        print("Podaj liczbe iteracji")
    e = input()
    e = float(e)
    if int(x) == 1:
        print("podaj przedzial \na:")
        a = input()
        print("\nb:")
        b = input()
        metodaBisekcji.medotaBisekcji(a, b, y, z, e)
    if int(x) == 2:
        print("podaj przedzial \na:")
        a = input()
        print("\nb:")
        b = input()
        sieczne.nowe_sieczne(a, b, y, z, e)
