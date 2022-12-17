#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    st = input("Введите строку: ")
    return st


def test_input(st):
    return st.isnumeric()


def str_to_int(st):
    return int(st)


def print_int(st):
    print(st)


if __name__ == '__main__':
    x = get_input()
    if test_input(x) == 1:
        x = str_to_int(x)
        print_int(x)
