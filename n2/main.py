from typing import List

from functions import *

def main():
    print("Простые числа до N:", get_primes(int(input("Введите число N: "))))
    print("Длина самой короткой строки:", shortest_string_length(list(input("Введите несколько слов через пробел: ").split())))
    print("Пересечение четных и нечетных:", intersect_even_odd(list(map(int, input("Введите числа через пробел: ").split()))))
    print("Факториал N:", factorial(int(input("Введите число N: "))))
    print("Сумма положительных чисел:", sum_positive(list(map(int, input("Введите числа через пробел: ").split()))))
    print("Удаление дубликатов:", remove_duplicates(list(map(int, input("Введите числа через пробел: ").split()))))
    print("Словарь с обратными значениями:", inverse_dict(int(input("Введите число N: "))))
    print("Строка с наибольшим количеством 'a' (латинской):", most_a_string(list(input("Введите несколько слов через пробел: ").split())))

    dict1 = eval(input("Введите первый словарь (например, {'a': 1, 'b': 2}): "))
    dict2 = eval(input("Введите второй словарь (например, {'c': 3, 'd': 4}): "))
    print("Объединение словарей(при одинаковых ключах второй значения из второго словаря имеют больший приоритет:\n", merge_dicts(dict1, dict2))

    print("Сумма нечетных чисел до N:", sum_odd_numbers(int(input("Введите число N: "))))

if __name__=="__main__":
    main()