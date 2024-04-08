import gausseMethod

def interface():
    zad2()

def zad2():
    m = gausseMethod.matrix()
    m.zad2()
    # if m.checkConvergence():
    #     print("gitara")
    m.gausse(1)

zad2()