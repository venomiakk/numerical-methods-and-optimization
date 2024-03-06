import metodaBisekcji
import sieczne
def interface(f1):
    print("1.Metoda bisekcji \n 2.Metoda siecznych")
    x = input()
    if int(x) == 1:
        print("podaj przedzial \n a:")
        a=input()
        print("\n b:")
        b=input()
        metodaBisekcji.medotaBisekcji(f1,a,b)
    if int(x) == 2:
        print("podaj przedzial \n a:")
        a = input()
        print("\n b:")
        b = input()
        sieczne.nowe_sieczne(f1, a, b)
