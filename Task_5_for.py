# Завдання 5
#     Дано одне число Price - ціна на 1 кг апельсин. 
#     Вивести вартість 1, 2, ... , 10 кг апельсин.
#     (Спробуйте вирішити задачу двома способами: циклом FOR та циклом WHILE)

def count_price():
    price = int(input("Введите цену за 1кг апельсин: "))
    
    for i in range(11):
        if i > 0:
            rezult_price = price * i
            print(i, "кг. апельсин", str(rezult_price), "грн.")
            i += 1
    return count_price()
count_price()