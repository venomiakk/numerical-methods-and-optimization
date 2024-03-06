import misc
def medotaBisekcji(funkcja, a,b):
    i =0
    f=funkcja
    x1=float(a)
    x2=float(b)
    x3=float((x1+x2)/2)
    x= misc.horner(x3, f)
    while (x != 0 and not misc.szacowanie_dokladnosci(x1 , x2 ,0.00000000000000001)) and i < 100:
        i += 1
        print(x1, " x1")
        print(x2, " x2")
        print(x3, " x3")
        if misc.horner(x3, f) * misc.horner(x1,f) < 0:
            x2 = x3
        else:
            x1 = x3
        x = misc.horner(x3, f)
        x3=float((x1+x2)/2)
    print("wynik: ", i, " ", x)

medotaBisekcji([2,5,0], 1, 3)






