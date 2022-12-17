#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    """
    Позволяет ввести строку
    """
    st = input("Введите строку: ")
    return st


def test_input(st):
    """
    Проверят можно ли преобразовать строку в число
    """
    return st.isnumeric()


def str_to_int(st):
    """
    Преобразует строку в число
    """
    return int(st)


def print_int(st):
    """
    Выводит на дисплей преобразованное число
    """
    print(st)


if __name__ == '__main__':
    x = get_input()
    if test_input(x) == 1:
        x = str_to_int(x)
        print_int(x)
