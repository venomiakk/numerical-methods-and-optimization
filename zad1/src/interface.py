import metodaBisekcji
def interface():
    print("1.Metoda bisekcji")
    x = input()
    if int(x) == 1:
        print("podaj przedzial \n a:")
        a=input()
        print("\n b:")
        b=input()
        metodaBisekcji.medotaBisekcji(a,b)

