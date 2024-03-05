import misc
def medotaBisekcji(a,b):
    i =0
    f=[1,3,-5,1]
    x= misc.horner((a+b)/2, f, 3)
    x1=a
    x2=b
    while x != 0 and i > 100:
        i+=1
        if misc.horner(x,f,3) * x1 > 0:
            x2=x
        else:
            x1=x
        x=misc.horner(x1+x2/2, f,3)
    print(x1,x2)






