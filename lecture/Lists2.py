#a = 2.46464
#b = 8.4646878
#print (round (a*b, 3))


#Задача №17. Решение в группах
#Дан список чисел. Определите, сколько в нем
#встречается различных чисел.
#Input: [1, 1, 2, 0, -1, 3, 4, 4]
#Output: 6
#inp = [1, 1, 2, 0, -1, 3, 4, 4]
#y = {*inp}
#print(len(y))


#Задача №19. Решение в группах
#Дана последовательность из N целых чисел и число
#K. Необходимо сдвинуть всю последовательность
#(сдвиг - циклический) на K элементов вправо, K –
#положительное число.
# Input: [1, 2, 3, 4, 5]
# k = 3
# Output: [4, 5, 1, 2, 3]
# b = [1, 2, 3, 4, 5]
# for i in range(2):
#     b.insert(0,b.pop())
#     print(*b)

# k = 3
# lst = [1, 2, 3, 4, 5]

#new_lst = lst[k:] + lst[0:k]
#print(new_lst)

# for i in range(k):
#     for a in range(len(lst) - 1):
#         temp = lst[a]
#         lst[a] = lst[a + 1]
#         lst[a + 1] = temp
#
# print(lst)

# mas = [1, 2, 3, 4, 5]
# k = 3
# # print(mas)
# for i in range(k-1):
#     last_el = mas.pop()
#     mas.insert(0, last_el)
#
# print(mas)


#Задача №21. Решение в группах
#Напишите программу для печати всех уникальных
#значений в словаре.
# lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII" : "S005"}, {"V" : "S009"}, {"VIII" : "S007"}]
#
# set_obj = set()
# for d_el in lst:
#     for val in d_el.values():
#         set_obj.add(val)
# print(set_obj)



#Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

lst = [0, -1, 5, 2, 3]
counter = 0
prev = lst[0]
for i in range(1, len(lst)):
    if lst[i] > prev:
        counter +=i
    prev = lst[i]
print(counter)
