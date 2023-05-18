#list_1 = []
#list_1 = list()
#list_1 = [1, 2, 5, 8]
#print(list_1)
# если не нужны скобки квадратные, запятые,точки можно перед list_1 поставить звездочку print(*list_1)

# цикл for
#for i in list_1:
#    print(i)
# можем узнать размер нашего списка
#print(len(list_1))
# обращение к нужному элементу нумерация начинаеться с (0)
#print(list_1[0])
#print(list_1[-1])

# добавление в список элеметна через функцию (append)
#list_1 = [1, 5]
#print(list_1)
#list_1.append(8)
#print(list_1)
#list_1.append(65)
#print(list_1)

# написание небольшой программы цикл (for)
#list_1 = []
#print(list_1)
#for i in range(7):
#    list_1.append(i)
#    print(list_1)

# Удаление последнего элемента из списка
#list_1 = [12, 7, -1, 21, 0]
#print(list_1.pop())
#print(list_1)
#print(list_1.pop())
#print(list_1)
#print(list_1.pop())
#print(list_1)

# Удаление конкретного элемента из списка
#list_1 = [12, 7, -1, 21, 0]
#print(list_1.pop(0))
#print(list_1)

# Добавление элемента на нужную пазицию
#list_1 = [12, 7, -1, 21, 0]
#print(list_1.insert(2, 11))
#print(list_1)

# Работа со срезами
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])                           # 1
# print(list_1[1])                           # 2
# print(list_1[len(list_1)-1])               #  10
# print(list_1[-5])                          #   6
# print(list_1[:])                           #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])                          #  [1, 2]
# print(list_1[len(list_1)-2])               #   9
# print(list_1[2:9])                         #   [3, 4, 5, 6, 7, 8, 9]
# print(list_1[0:len(list_1):6])             #   [1, 7]
# print(list_1[::6])                         #   [1, 7]

# кортеж

# t = ()
# print(type(t))
# t = (2, 5, 7,)
# print(type(t))
#
# v = [5, 7, 9]
# print(v)
# print(type(v))
#
# v = tuple(v)
# print(v)
# print(type(v))

# множественное присваивание примеры
# a,b = 1, 2
# a = b = 1

# a,b,c, = v
# print(a,b,c)

#t = (1, 2, 7, 5, 4)
#print(t[2])      #вывод картеж по индексу
#for i in t:       # можем пройтись при помощи тикла for
#    print(i)
#
#for i in range(len(t)):
#    print(t[i])

# Словари
# dictionary = {}
# dictionary = {'up': 'вверх', 'left': 'лево', 'down': 'низ', 'right': 'право'}
# print(dictionary)    #{'up': 'вверх', 'left': 'лево', 'down': 'низ', 'right': 'право'}
#print(dictionary['left'])   # 'лево'

# Типы ключей могут отличаться
#
# print(dictionary['up'])     # 'вверх'
# print(dictionary['right'])  # 'право'
# dictionary['left'] = 'лево'
# print(dictionary['left'])    #  'лево'
# print(dictionary['type'])    #KeyError : 'type' нет такого ключа и будет ошибка

# del dictionary['left']          #удаление элемента
# for item in dictionary:         # for (k, v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))

# up: вверх
# down: низ
# right: право

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors)                        #{'red', 'blue', 'green'}
# colors.add('red')                   #при помощи add добовляем значение
# print(colors)                        #{'red', 'blue', 'green'}
# colors.add('grey')
# print(colors)                         #{'red', 'blue', 'green','grey'}
# colors.remove('red')
# print(colors)                          #{'blue', 'green','grey'}
# colors.discard('red')           # функция провереят значения и если нет такого значения то прохотит не выдовая ошибку
# print(colors)
# colors.clear()                 #удаление всего множества всех значений
# print(colors)                  # set()

# Операции со Множествами
# a = {1, 2, 4, 7, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# u = a.union(b)               # объединение
# i = a.intersection(b)        # пересечения те элементы которые повторяються
# d1 = a.difference(b)          #
# dr = b.difference(a)            #
# q = a.union(b).difference(a.intersection(b))       # {1, 4, 5, 7, 13, 21}
# print(q)

# заморенное множество

# a = {1, 8, 6}
# b = frozenset(a)        # frozenset- замораживает и не можем изменять мночество
# print(b)

# Герератор списков
# Создать список, состоящий из четных чисел в диапозоне от 1 до 100.
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
#     print(list_1)
# Это примемер можно записать так:

# list_1 = [i for i in range(1, 101)]
# print(list_1)

# # добавить в задачу (только четные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]
# print(list_1)

# # Создать пару каждому из чисел (Кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
# print(list_1)

# Можно умножать, делить, вычетать, прибовлять
# Умножить значение на (2)
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1)
a = ("b")
b = 3
print(a)



