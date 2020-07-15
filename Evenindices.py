# Задача «Четные индексы»
# Условие
# Выведите все элементы списка с четными индексами
a = [1, 2, 3, 4, 5]
s = a[0]
for s in range(len(a)):
    if s % 2 == 0:
        print(a[s])

a = [4, 5, 3, 4, 2, 3]
for s in range(len(a)):
    if s % 2 == 0:
        print(a[s])

a = [9, 4, 5, 2, 3]
for s in range(len(a)):
    if s % 2 == False:
        print(a[s])

a = [6]
for s in range(len(a)):
    if s % 2 != True:
        print(a[s])

a = [7, 8]
for s in range(len(a)):
    if s % 2:
        print(a[s])

a = [1, 2, 3]
for s in range(len(a)):
    if s % 2 :
        print(a[s + 1])

a = [90, 45, 3, 43]
for s in range(len(a)):
    if s % 2 :
        print(a[s])
