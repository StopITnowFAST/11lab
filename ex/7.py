import math


def cylinder():
	r = float(input())
	h = float(input())
	# площадь боковой поверхности цилиндра:
	side = 2 * math.pi * r * h
	# площадь одного основания цилиндра:
	circle = math.pi * r**2
	# полная площадь цилиндра:
	full = side + 2 * circle
	return full

	
square = cylinder()
print(square)
