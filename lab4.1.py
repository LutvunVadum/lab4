import math

def f1(x):
    y = abs(math.sin(2 * x) + math.cos(3 * x + 1) + math.tan(abs(x) + 0.7)) + math.log10(abs(x - 4))
    return (y)

x1 = float(input("Введіть значення х:"))
y = f1(x1)
print(y)
