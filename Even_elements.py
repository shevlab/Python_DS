# Списки
# Задача «Четные элементы»

# Условие
# Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!

#a = [1, 2, 2, 3, 3, 3, 4,]
a = [44, -51, 32, -60, -7, -67, 62, 91, 26, -14]

for i in range(len(a)):
    s = int(a[i])
    if s % 2 == 0:
        print(s)

