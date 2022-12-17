#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def positive():
    """
    Сообщает что число положительное
    """
    print("Положительное")


def negative():
    """
    Сообщает что число отрицательное
    """
    print("Отрицательное")


def test():
    """
    Проверяет знак числа
    """
    x = int(input("Введите целое число: "))
    if x > 0:
        positive()
    else:
        negative()


if __name__ == '__main__':
    test()