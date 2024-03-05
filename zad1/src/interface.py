import metodaBisekcji
import sieczne
def interface():
    print("1.Metoda bisekcji \n 2.Metoda siecznych")
    x = input()
    if int(x) == 1:
        print("podaj przedzial \n a:")
        a=input()
        print("\n b:")
        b=input()
        metodaBisekcji.medotaBisekcji(a,b)
    if int(x) == 2:
        print("podaj przedzial \n a:")
        a = input()
        print("\n b:")
        b = input()
        sieczne.metoda_siczenych([1, 3, -5, 1], a, b)
