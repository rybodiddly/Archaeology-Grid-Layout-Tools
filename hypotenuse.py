from math import sqrt
print('Input sides A & B of triange:')
a = float(input('a: '))
b = float(input('b: '))

c = sqrt(a**2 + b**2)
print('Length of side C (hypotenuse):', c)