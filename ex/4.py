def rectangle():
	a = float(input("Ширина %s: " % figure))
	b = float(input("Высота %s: " % figure))
	print(f"Площадь: {a * b}")


def triangle():
	a = float(input("Основание %s: " % figure))
	h = float(input("Высота %s: " % figure))
	print(f"Площадь: {0.5 * a * h}")


figure = input("1-прямоугольник, 2-треугольник: ")
if figure == '1':
	rectangle()
elif figure == '2':
	triangle()
