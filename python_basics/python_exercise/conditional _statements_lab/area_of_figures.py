from math import pi
geometric_shape = input()
a = float(input())
area = 0
if geometric_shape == 'square':
    area = a * a
elif geometric_shape == 'rectangle':
    b = float(input())
    area = a * b
elif geometric_shape == 'circle':
    area = pi * a * a
elif geometric_shape == 'triangle':
    h = float(input())
    area = a * h / 2
print(f"{area:.3f}")
