"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

#1.
import random

OPERATIONS = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
}

def calculator(expr):
    if isinstance(expr, tuple):
        return OPERATIONS[expr[1]](calculator(expr[0]), calculator(expr[2]))

    return expr

print(calculator(((1, '+', 2), '*', 3)))


#2. Уже ближе
def ret(s):
    operations = ['+', '-', '*', '/']
    operation = input('Введите операцию: ')
    num1 = input('Введите первое число: ')
    num2 = input('Введите второе число: ')
    s = str(s)
    if s.isdigit():
        return float(s)
    for c in ('-','+','*','/'):
        left, op, right = s.partition(c)
        if op == '*':
            return ret(left) * ret(right)
        elif op == '/':
            return ret(left) / ret(right)
        elif op == '+':
            return ret(left) + ret(right)
        elif op == '-':
            return ret(left) - ret(right)

#3. Верное решение

def ret():
    operations = ['+', '-', '*', '/']
    operation = input('Введите операцию: ')
    num1 = input('Введите первое число: ')
    num2 = input('Введите второе число: ')
    if operation == 0:
        return None
    elif operation in operations:
        if operation == operations[0]:
            result = int(num1) + int(num2)
            return print(result), ret()
        elif operation == operations[1]:
            result = int(num1) - int(num2)
            return print(result), ret()
        elif operation == operations[2]:
            result = int(num1) * int(num2)
            return print(result), ret()
        elif operation == operations[3]:
            if num2 == "0":
                return print("Нельзя делить на ноль"), ret()
            else:
                result = int(num1) / int(num2)
                return print(result), ret()
if __name__ == "__main__":
    ret()


"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def recur(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        alt = num % 10
        num = num // 10
        if alt % 2 == 0:
            even += 1
        else:
            odd -= 1
        return recur(num, even, odd)

try:
    NUMB = int(input("Введите натуральное число: "))
    print(f"Количество четных и нечетных цифр в числе: {recur(NUMB)}")
except ValueError:
    print("Вы вместо числа ввели строку. Исправьтесь")


"""
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""


"""Рекурсия"""
def rev (numb):
    rest_numb, numeral = divmod(numb, 10)
    if rest_numb == 0:
       return str(numeral)
    else:
        return str(numeral) + str(rev(rest_numb))

number = int(input("Введите числоб которое требуется перевернуть:"))
print(f'Перевернутое число:{rev(number)}')


'''Через тернарный оператор'''
def rev(num):
    return str(num) if num < 10 else str(num % 10) + rev(num // 10)


"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def rec(elem):
    return 0 if elem == 0 else 1 + rec(elem - 1 ) / -2

COUNT = int(input("Введите количество элементов:"))
print(f'Количество элементов: {COUNT}, их сумма: {rec(COUNT)}')



"""
Задание 5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
Пример:
32 -   33 - ! 34 - " 35 - # 36 - $ 37 - % 38 - & 39 - ' 40 - ( 41 - )
42 - * 43 - + 44 - , 45 - - 46 - . 47 - / 48 - 0 49 - 1 50 - 2 51 - 3
52 - 4 53 - 5 54 - 6 55 - 7 56 - 8 57 - 9 58 - : 59 - ; 60 - < 61 - =
62 - > 63 - ? 64 - @ 65 - A 66 - B 67 - C 68 - D 69 - E 70 - F 71 - G
72 - H 73 - I 74 - J 75 - K 76 - L 77 - M 78 - N 79 - O 80 - P 81 - Q
82 - R 83 - S 84 - T 85 - U 86 - V 87 - W 88 - X 89 - Y 90 - Z 91 - [
92 - \ 93 - ] 94 - ^ 95 - _ 96 - ` 97 - a 98 - b 99 - c 100 - d 101 - e
102 - f 103 - g 104 - h 105 - i 106 - j 107 - k 108 - l 109 - m 110 - n 111 - o
112 - p 113 - q 114 - r 115 - s 116 - t 117 - u 118 - v 119 - w 120 - x 121 - y
122 - z 123 - { 124 - | 125 - } 126 - ~ 127 - 
Решите через рекурсию. В задании нельзя применять циклы.
Допускается исп-е встроенных ф-ций
"""
import sys

sys.setrecursionlimit(5000)

def atl(ASCII=32):
    if ASCII == 128:
        return True
    print(f"{ASCII} - {atl(ASCII)}", end=" ")
    if (ASCII - 31) % 10 == 0:
        print("\n")

    atl(ASCII + 1)

atl()


"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def recur(count, numb):
    print(f"Попытка №{count}")
    a = int(input("Введите число от 0 до 100: "))
    if count == 10 or a == numb:
        if a == numb:
            print("Верно!")
        print(f'Загаданное число: {numb}')
    else:
        if a > numb:
            print(f"Загаданное число ментше чем {numb}")
        else:
            print(f"Загаданное число больше чем {numb}")
        recur(count + 1, numb)

recur(1, random.randint(0, 100))





"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def recur(numb):
    if numb == 1:
        return numb
    else:
        return recur(numb - 1) + numb


try:
    NUMB = int(input("Введите число: "))
    if recur(NUMB) == NUMB * (NUMB + 1) / 2:
        print('Равенство верно')
except ValueError:
    print("Вместа числа, ввели число. Исправьте.")
