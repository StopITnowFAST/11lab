def rectangle():
	a = float(input("Ширина: "))
	b = float(input("Высота: "))
	print(f"Площадь: {a * b}")


def triangle():
	a = float(input("Основание: "))
	h = float(input("Высота: "))
	print(f"Площадь: {0.5 * a * h}")

figure = input("1-прямоугольник, 2-треугольник: ")
if figure == '1':
	rectangle()
elif figure == '2':
	triangle()
