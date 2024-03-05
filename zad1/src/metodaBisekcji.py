import misc
def medotaBisekcji(a,b):
    i =0
    f=[1,3,-5,1]
    x1=float(a)
    x2=float(b)
    x3=float((x1+x2)/2)
    x= misc.horner(x3, f, 3)
    while (x != 0 and not misc.szacowanie_dokladnosci(x1 , x2 ,0.00000000000000001)) and i < 100:
        i += 1
        print(x1, " x1")
        print(x2, " x2")
        print(x3, " x3")
        if misc.horner(x3, f, 3) * misc.horner(x1,f,3) < 0:
            x2 = x3
        else:
            x1 = x3
        x = misc.horner(x3, f, 3)
        x3=float((x1+x2)/2)
    print("wynik: ", i, " ", x)







