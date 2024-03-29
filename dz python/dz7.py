"""
На маленьких данных доработка показывает примерно такие же результаты, доработка эффективна при работе с большим
массивом данных:
# Пузырьковая сортировка 10 эл-в: 0.07786649999999999
# Пузырьковая сортировка 100 эл-в: 3.3387645
# Пузырьковая сортировка 1000 эл-в: 92.39562020000001
**************************************************************
# Пузырьковая сортировка доработаная, 10 эл-в: 0.0783801
# Пузырьковая сортировка доработаная, 100 эл-в: 3.2665108999999997
# Пузырьковая сортировка доработаная, 1000 эл-в: 91.0140653
"""
from random import randint
from timeit import timeit

numbers = [randint(-100, 100) for _ in range(1000)]

 
def bubble_sort(nums):
    n = 1
    print(nums)
    while n < len(nums):
        for i in range(len(nums) - n):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_sorting = True
        n += 1
    return print(nums)


def bubble_sort_2(nums):
    is_sorting = True
    n = 1
    print(nums)
    while is_sorting:
        while n < len(nums):
            for i in range(len(nums) - n):
                is_sorting = False
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    is_sorting = True
            n += 1
    return print(nums)


print(f'Пузырьковая сортировка 10 эл-в: {timeit("bubble_sort(numbers[:])", globals=globals(), number=1000)}')
# Пузырьковая сортировка 10 эл-в: 0.07786649999999999
# Пузырьковая сортировка 100 эл-в: 3.3387645
# Пузырьковая сортировка 1000 эл-в: 92.39562020000001
print(f'Пузырьковая сортировка доработаная, 1000 эл-в: {timeit("bubble_sort_2(numbers[:])", globals=globals(), number=1000)}')
# Пузырьковая сортировка доработаная, 10 эл-в: 0.0783801
# Пузырьковая сортировка доработаная, 100 эл-в: 3.2665108999999997
# Пузырьковая сортировка доработаная, 1000 эл-в: 91.0140653


#------------------------------------------------------
"""
Гномья сортировка, массив из 10 эл-в: 0.008193800000000001
Гномья сортировка, массив из 100 эл-в: 0.5651402000000001
Гномья сортировка, массив из 1000 эл-в: 68.85820460000001
"""
from random import randint
from timeit import timeit


def gnome_sort(lst, m):
    idx = 1
    i = 0
    while i < len(lst) - 1:
        if lst[i] <= lst[i + 1]:
            i, idx = idx, idx + 1
        else:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i -= 1
            if i < 0:
                i, idx = idx, idx + 1
    return lst[m]


m = 5
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Гномья сортировка, массив из 10 эл-в: {timeit("gnome_sort(my_data[:], m)", globals=globals(), number=1000)}')

m = 50
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Гномья сортировка, массив из 100 эл-в: {timeit("gnome_sort(my_data[:], m)", globals=globals(), number=1000)}')


m = 500
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Гномья сортировка, массив из 1000 эл-в: {timeit("gnome_sort(my_data[:], m)", globals=globals(), number=1000)}')


#------------------------------------------------------
"""
Поиск медианы без сортировки, массив из 10 эл-в: 0.0017420000000000005
Поиск медианы без сортировки, массив из 100 эл-в: 0.07501809999999999
Поиск медианы без сортировки, массив из 1000 эл-в: 6.4795162
"""
from random import randint
from timeit import timeit


def no_sort_median(lst):

    for i in range(len(lst) // 2):
        lst.remove(max(lst))

    return max(lst)


m = 5
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Поиск медианы без сортировки, массив из 10 эл-в: {timeit("no_sort_median(my_data[:])", globals=globals(), number=1000)}')

m = 50
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Поиск медианы без сортировки, массив из 100 эл-в: {timeit("no_sort_median(my_data[:])", globals=globals(), number=1000)}')

m = 500
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Поиск медианы без сортировки, массив из 1000 эл-в: {timeit("no_sort_median(my_data[:])", globals=globals(), number=1000)}')

#------------------------------------------------------

"""
Поиск медианы встроенной ф-й, массив из 10 эл-в: 0.0006323999999999982
Поиск медианы встроенной ф-й, массив из 100 эл-в: 0.003054099999999997
Поиск медианы встроенной ф-й, массив из 1000 эл-в: 0.0725292
**********************************************************************
Поиск медианы без сортировки, массив из 10 эл-в: 0.0017420000000000005
Поиск медианы без сортировки, массив из 100 эл-в: 0.07501809999999999
Поиск медианы без сортировки, массив из 1000 эл-в: 6.4795162
**********************************************************************
Гномья сортировка, массив из 10 эл-в: 0.008193800000000001
Гномья сортировка, массив из 100 эл-в: 0.5651402000000001
Гномья сортировка, массив из 1000 эл-в: 68.85820460000001
Дольше всего работала гномья сортировка, быстрее всего -- встроенная ф-ция median
"""
from random import randint
from statistics import median
from timeit import timeit


def median_sort(lst):
    return median(lst)


m = 5
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Поиск медианы встроенной ф-й, массив из 10 эл-в: {timeit("median_sort(my_data[:])", globals=globals(), number=1000)}')

m = 50
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Поиск медианы встроенной ф-й, массив из 100 эл-в: {timeit("median_sort(my_data[:])", globals=globals(), number=1000)}')

m = 500
my_data = [randint(-100, 100) for i in range(2 * m + 1)]
print(f'Поиск медианы встроенной ф-й, массив из 1000 эл-в: {timeit("median_sort(my_data[:])", globals=globals(), number=1000)}')