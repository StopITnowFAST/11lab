#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


def test():
    x = int(input("Введите целое число: "))
    if x > 0:
        positive()
    else:
        negative()


if __name__ == '__main__':
    test()