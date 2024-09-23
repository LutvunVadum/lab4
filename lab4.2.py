import math
x = float(input("Введіть значення х:"))
y = float(input("Введіть значення y:"))

f = math.pow((pow(x,3) + pow(y,3)), 1/4) + math.sin(3*x + 1) + math.log10(math.fabs(x)) - pow(math.e,(y-x))

print(f)