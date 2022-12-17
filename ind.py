#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
# группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
# следующие действия:
# 1. ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# 2. записи должны быть упорядочены по алфавиту;
# 3. вывод на дисплей фамилий и номеров групп для всех студентов, имеющих хотя бы одну оценку 2;
# 4. если таких студентов нет, вывести соответствующее сообщение.


def add(mas):
    """
    Ввести данные студента в словарь
    """

    name = input("Фамилия и инициалы? ")
    group = input("Номер группы? ")
    buf = [int(a) for a in input().split()]
    lmarks = list(filter(lambda x: 0 < x < 6, buf))
    if len(lmarks) != mas:
        error()

    return {
        'name': name,
        'group': group,
        'marks': lmarks,
    }


def show(staff):
    """
    Вывод записей всего словаря
    """
    if staff:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "№",
                "Ф.И.О.",
                "Группа",
                "Успеваемость"
            )
        )
        print(line)

        for idx, student in enumerate(staff, 1):
            lmarks = student.get('marks', '')
            print(
                '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group', ''),
                    ' '.join(map(str, lmarks)),
                )
            )
        print(line)
    else:
        print("Список пуст")


def marks(staff):
    """
    Вывод фамилий и номеров групп, студентов имеющих 2
    """
    count = 0
    line = '+-{}-+-{}-+'.format(
        '-' * 30,
        '-' * 10
    )
    for student in staff:
        if 2 in student.get('marks'):
            count += 1
            if count == 1:
                print(line)
            print(
                '| {:<30} | {:^10} |'.format(
                    student.get('name', ''),
                    student.get('group', ''),
                )
            )
            print(line)

    if count == 0:
        print("Студенты не найдены.")


def error():
    """
    Ошибка при выполнении программы
    """
    print("Что-то пошло не так", file=sys.stderr)
    exit()


def main():
    """
    Главная функция программы
    """
    n = 5
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            student = add(n)
            students.append(student)
            if len(students) > 1:
                students.sort(key=lambda item: item.get('name', ''))

        elif command == 'show':
            show(students)

        elif command == 'marks':
            marks(students)


if __name__ == '__main__':
    main()
