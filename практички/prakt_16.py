#Акулов Артём, вариант №4, практичка № 16


import prakt_16_1  

N = int(input("Введите количество чисел в списке: "))
numbers = [float(input(f"Введите число {i + 1}: ")) for i in range(N)]
znach = float(input("Введите пороговое значение (znach): "))

result = prakt_16_1.sum_less_than(numbers, znach)
print(f"Сумма элементов, меньших {znach}: {result}")