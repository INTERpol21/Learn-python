"""
Задание 1.
Для каждой из трех функций выполнить следующее:
1) для каждого выражения вместо символов !!! укажите сложность.
2) определите сложность алгоритма в целом (Сложность: !!!).
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- Сложность нужно указать только там, где есть !!!
-- Сложности встроенных функций и операций нужно искать
    в таблицах (см. материалы к уроку).
"""

from random import sample


##############################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.
    Алгоритм 1:
    Создать множество из списка
    Сложность: O(len)
    """
    lst_to_set = set(lst_obj)  # O(len)
    return lst_to_set  # O(1)


##############################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 2:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах
    Сложность: O(n)
    """
    for j in range(len(lst_obj)):          #  O(n)
        if lst_obj[j] in lst_obj[j+1:]:    #  O(len)
            return False                   # O(1)
    return True                            # O(1)


##############################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 3:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: O(N Log N)
    """
    lst_copy = list(lst_obj)                 # O(n)
    lst_copy.sort()                          # O(N Log N)
    for i in range(len(lst_obj) - 1):        # O(n))
        if lst_copy[i] == lst_copy[i+1]:     # O(1)
            return False                     # O(1)
    return True                              # O(1)


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))


#----------------------------------------------------------------------------------------------------

"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

def line(alt):
    min = alt[0]            #O(1)
    for a in alt[1:]:       #O(n)
        if min > a:         #O(1)
            min = a         #O(1)
    return min              #O(1)

print(line([1, 2, 3, 4, 5, 20]))


def line2(alt):
    min = a[0]                  #O(1)
    for a in alt:               #O(n)
        for b in alt:           #O(n)
            if a<b:             #O(1)
                if a < min:       #O(1)
                     a = 1     #O(1)
            else:
                if b < min:      #O(1)
                    min < b       #O(1)
    return min

print(line([1, 2, 3, 4, 5, 20]))


"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

#1  #O(N LOG N )
dictionary = {1: 1000, 2: 500,3: 5000,4: 2000}

sorted_values = sorted(dictionary.values()) # Упорядочивания значений словаря #O(N LOG N)
sorted_dictionary = {}                          #Создаем пустой словарь для заполнения  #O(1)

for i in sorted_values:  #O(N)
    for k in dictionary.keys():      #O(N)
        if dictionary[k] == i:           #O(1)
            sorted_dictionary[k] = dictionary[k]   #O(1)
            break
print(sorted_dictionary)


#2  #O(N)

from functools import cmp_to_key  #O(1)


def mine(x, y):              #O(1)
    if x[1] != y[1]:           #O(1)
        return x[1] > y[1]       #O(1)
    else:
        return x[0] > y[0]          #O(1)

a = []
a.append(["1", 1000])
a.append(["2", 500])
a.append(["3", 5000])
a.append(["4", 2000])

def mine(a,b):           #O(1)
    if a[1] > b[1]:      #O(N)
        return 1         #O(1)
    elif a[1] < b[1]:    #O(1)
        return -1           #O(1)
    else:
        if a[0] > b[0]:      #O(1)
            return 1         #O(1)
        else:
            return 0         #O(1)

print(sorted(a, key=cmp_to_key(mine)))


#3 O(n LOG n)

dict1 = {1: 1000, 2: 500,3: 5000,4: 2000}    #O(1)
sorted_dict = {}                 #O(1)
sorted_keys = sorted(dict1, key=dict1.get)  # [1, 3, 2]  #O(N LOG N)

for w in sorted_keys:                     #O(N)
    sorted_dict[w] = dict1[w]           #O(1)

print(sorted_dict)              #O(1)

"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""



dictionary = {1: 1000, 2: 500,3: 5000,4: 2000}

users = {}
'''   id       login  password  is_activate'''
users['1'] = ('first', 'pass1', True)
users['2'] = ('second', 'pass2', False)
users['3'] = ('three', 'pass3', False)

def view_users():
    '''сложность линейная O(N)'''
    print(f'введите номер пользователя для прооверки')
    for id_user, value in users.items():  # O(N)
        login, *_ = value
        print(f'{id_user} {login}')
    id_user = input()
    user = users.get(id_user)  # O(1)
    if user:
        if not user[2]:
            print(f'{user[0]} - вам необходимо пройти активацию')
            question = input(f'Активируем аккаунт {user[0]}? да/нет\n')
            if question.lower() in ['да', 'д', 'y', 'yes']:  # O(N)
                users[id_user] = (user[0], user[1], True)
                print(f'аккаунт {user[0]} активирован')
            else:
                print(f'Активация не совершена доступ для {user[0]} запрещен')
        else:
            print(f'Добро пожаловать! {user[0]}')
    else:
        print(f'Пользователя под таким номером - {id_user} не существует')

#view_users()

def view_users2():
    '''сложность O(N^2) квадратичная'''
    for user_tup in users.values():
        for val in user_tup:
            if isinstance(val, bool):
                if val == False:
                    print(f'активируйте учетную запись пользователя {user_tup[0]}')
                else:
                    print(f'учетная запись пользователя {user_tup[0]} активирована')


view_users2()



def check_user(user):
    if user[2]:
        print(f'пользователь {user[0]} активирован')
    else:
        print(f'пользователь {user[0]} не активирован. Пройдите активацию')


users = list(users.values())


def check_1(users):
    '''сложность константная O(1)'''
    while len(users) > 0:   # O(1)
        user = users.pop()  # O(1)
        check_user(user)

def check_2(users):
    '''линейная O(N)'''
    for user in users:   #  O(1)
        check_user(user)

def check_4(users):
    '''линейно логарифмическая O(N log N)'''
    sorted(users)  # O(N log N)
    print(users)

    """
    Задание 5. На закрепление навыков работы со стеком
    Реализуйте собственный класс-структуру "стопка тарелок".
    Мы можем складывать тарелки в стопку и при превышении некоторого значения
    нужно начать складывать тарелки в новую стопку.
    Структура должна предусматривать наличие нескольких стопок.
    Создание новой стопки происходит при достижении предыдущим
    стеком порогового значения.
    После реализации структуры, проверьте ее работу на различных сценариях.
    Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
    --реализуйте по аналогии с примером, рассмотренным на уроке
    --создание нового стопки можно реализовать добавлением нового пустого массива
    в массив стопок (lst = [[], [], [], [],....]).
    """

class Stack_plate():
    def __init__(self):
        self.limit = 3
        self.stack = [[]]

    def append_val(self, val):
        '''append new value'''
        if len(self.stack[-1]) > self.limit:
            new_inner = []
            new_inner.append(val)
            self.stack.append(new_inner)
        else:
            self.stack[-1].append(val)

    def get_val(self):
        '''get value'''
        res = self.stack[-1][-1]
        del self.stack[-1][-1]
        if len(self.stack[-1]) < 1:
            del self.stack[-1]
        return res


    def __str__(self):
        return str(self.stack)

st = Stack_plate()
st.append_val('345')
st.append_val('344645')
st.append_val('39095')
st.append_val(678)
st.append_val(7)
st.append_val('34jklj5')
st.append_val('test')


for _ in range(3):
    print(f'get values {st.get_val()}')
print(st)





"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""




class Task_board(_):
    def __init__(self, tasks):
        self.main_queue = _()
        self.complete_queue = _()
        self.uncomplete_queue = _()
        self.fill_main_queue(tasks)

    def fill_main_queue(self, tasks):
        for task in tasks:
            self.main_queue.to_queue(task)


    def solving_tasks(self):
        '''решение входящих задач'''
        while not self.main_queue.is_empty():
            task = self.main_queue.from_queue()
            if task:
                self.complete_queue.to_queue(task)
            else:
                self.uncomplete_queue.to_queue(task)

    def sloving_uncomplete_tasks(self):
        '''решение не решенных задач'''
        temp = []
        for _ in self.uncomplete_queue:
            temp.append(f'task is over')
        self.uncomplete_queue.clear()
        for _ in temp:
            self.complete_queue.to_queue(task)



    def pirnter_tasks(self):
        print(f'все вновь поступившие не обработанные задачи {self.main_queue.all_elements()}')
        print(f'все завершенные задачи {self.complete_queue.all_elements()}')
        print(f'все задачи на доработку {self.uncomplete_queue.all_elements()}')


Tb = Task_board([True, False, 'test'])
Tb.pirnter_tasks()
print('-'*30)
Tb.solving_tasks()
Tb.pirnter_tasks()
print('*'*30)



"""
Задание 7. На закрепление навыков работы с деком
В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'
Но могут быть и такие палиндромы, как 'молоко делили ледоколом'
Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром и в таких строках (включающих пробелы)
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""

class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def pal_checker(string):
    dc_obj = DequeClass()
    string = string.replace(' ', '')  # доработка
    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))