#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def mult():
    x = 1
    a = 1
    while a != 0:
        a = int(input("Число для умножения: "))
        if a == 0:
            break
        x = x * a
        print(x)
    return(x)


if __name__ == '__main__':
    print("Полученное число: ", mult())
