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


