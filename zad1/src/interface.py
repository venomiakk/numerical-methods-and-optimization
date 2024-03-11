import metodaBisekcji
import sieczne
def interface():
    print("1.wielomian \n 2.funkcja trygonometryczna\n 3.funkcja wykladnicza\n 4.funkcja zlozona")
    y = input()
    print("1.Metoda bisekcji \n 2.Metoda siecznych")
    x = input()
    if int(x) == 1:
        print("podaj przedzial \n a:")
        a = input()
        print("\n b:")
        b = input()
        metodaBisekcji.medotaBisekcji(a, b, y)
    if int(x) == 2:
        print("podaj przedzial \n a:")
        a = input()
        print("\n b:")
        b = input()
        sieczne.nowe_sieczne(a, b, y)
