import math
x = float(input("Введіть значення х:"))
y = float(input("Введіть значення y:"))

f = math.pow((math.pow(x,3) + math.pow(y,3)), 1/4) + math.sin(3*x + 1) + math.log10(math.fabs(x)) - math.pow(math.e,(y-x))

print(f)
