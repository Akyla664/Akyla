#Акулов Артём, вариант №4, практичка № 13
import random


N = int(input("Введите количество чисел (N): "))
numbers = [random.randint(-100, 100) for _ in range(N)] 


file_name = "numbers.txt"
with open(file_name, "w") as file:
    file.write(" ".join(map(str, numbers)))

with open(file_name, "r") as file:
    data = file.read().split()  
    numbers_from_file = list(map(int, data))  


opposite_pairs_count = 0
seen_numbers = set()

for number in numbers_from_file:
    if -number in seen_numbers:  
        opposite_pairs_count += 1
    seen_numbers.add(number) 


print(f"Количество пар противоположных чисел: {opposite_pairs_count}")