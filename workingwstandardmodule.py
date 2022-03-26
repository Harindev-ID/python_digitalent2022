from math import ceil, floor, trunc, hypot

x = 1.4
y = 2.6
z = 3.5

print(floor(x), floor(y), floor(z))
print(floor(-x), floor(-y), floor(-z))

print(ceil(x), ceil(y), ceil(z))
print(ceil(-x), ceil(-y), ceil(-z))

print(trunc(x), trunc(y), trunc(z))
print(trunc(-x), trunc(-y), trunc(-z))

print(hypot(4,3))
print(hypot(x,y))
