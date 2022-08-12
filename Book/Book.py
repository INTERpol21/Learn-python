def binary_search(list, item):       # Создаем функцию бинарного поиска, в переменных low/high
    low = 0                       # определяем границы списка где будет выполняться поиск
    high = len(list)-1

    while low <= high:              #Повторяем поиск по среднему числу списка, пока он не сократиться до одного
        mid = (low + high)
        guess = list[mid]
        if guess == item:           # значение найдено = возрашаем мид
            return mid
        if guess > item:            # много
            high = mid - 1
        else:
            low = mid + 1           #мало
            return None            #значение не существует=вернуть None

    my_list = [1, 3, 5, 7, 9]       #ТЕСТОВЫЕ ДАННЫЕ

    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))



#------------------------------------------------------------------------

def find_Smallest (arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5, 3, 6, 2, 10]))

#------------------------------------------------------------------------

def sum(i):
    if i == []:
        return 0
    return i[0] + sum(i[1:])

def count(i):
    if i == []:
        return 0
    return 1 + count(i[1:])

def max(list):
    if len == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

#------------------------------------------------------------------------


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pilot = arr[0]
        less = [i for i in arr[1:] if i <= pilot]
        greater = [i for i in arr[1:] if i > pilot]
        return quicksort(less) + [pilot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))



#------------------------------------------------------------------------
