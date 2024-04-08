import gausseMethod

print("Wybor elementu glownego\n1. Czesciowy\n2. Pelny")
inp = input()

m = gausseMethod.matrix()
m.zad2()

# 1 - partly, 2 - fully
m.gausse(int(inp))
