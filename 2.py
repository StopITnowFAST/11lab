#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PI = 3.14


def circle(r):
    """
    Возвращает площать круга
    """
    return PI * (r * r)


def cylinder():
    """
    Просчитывает площадь цилиндра
    """
    h = float(input("Введите высоту цилиндра: "))
    r = float(input("Введите радиус цилиндра: "))
    ch = int(input("1 - S боковой поверхности цилиндра\n2 - S цилиндра\n"))

    if ch == 1:
        s = 2 * PI * r * h
    elif ch == 2:
        s = 2 * PI * r * h
        s = s + 2 * (circle(r))
    print("Площадь = ", s)


if __name__ == '__main__':
    cylinder()