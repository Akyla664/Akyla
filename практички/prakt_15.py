#Акулов Артём, вариант №4, практичка № 15


def reverse_digits(number):
    """
    Возвращает число с цифрами в обратном порядке.
    
    :param number: Натуральное число.
    :return: Число с цифрами в обратном порядке.
    """
    return int(str(number)[::-1]) 

input_file_name = "input.txt"
output_file_name = "output.txt"

try:
    
    with open(input_file_name, "r", encoding="utf-8") as file:
        numbers = file.read().split()  

    reversed_numbers = [reverse_digits(int(num)) for num in numbers]

  
    with open(output_file_name, "w", encoding="utf-8") as file:
        file.write(" ".join(map(str, reversed_numbers)))  
    print(f"Преобразованные числа успешно записаны в файл: {output_file_name}")

except FileNotFoundError:
    print(f"Ошибка: Файл {input_file_name} не найден.")
except ValueError:
    print("Ошибка: Файл содержит некорректные данные (ожидались натуральные числа).")