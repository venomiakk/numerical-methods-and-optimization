import metodaBisekcji
import sieczne
def interface():
    print("Wybierz funkcje:\n1. Wielomian \n2. Funkcja trygonometryczna\n3. Funkcja wykladnicza\n4. Funkcja zlozona")
    y = input()
    print("Wybierz metode:\n1. Metoda bisekcji \n2. Metoda siecznych")
    x = input()
    print("Wybierz warunek zatrzymania:\n1. Ilosc iteracji\n2. Dokładność wyznaczania pierwiastka")
    z = input()
    z = int(z)
    if z==2 :
        print("Podaj dokladnosc: ")
    else:
        print("Podaj liczbe iteracji")
    e = input()
    e = float(e)
    if int(x) == 1:
        print("Podaj przedzial \na:")
        a = input()
        print("b:")
        b = input()
        metodaBisekcji.metodaBisekcji(a, b, y, z, e)
    if int(x) == 2:
        print("Podaj przedzial \na:")
        a = input()
        print("b:")
        b = input()
        sieczne.oblicz(a, b, y, z, e)
