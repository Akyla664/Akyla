#Акулов Артём, вариант №4, практичка № 19, Основной модуль
import input_module
import processing_module
import output_module

def main():
    print("Выберите задачу:")
    print("1. Вычисление выражения z")
    print("2. Вычисление выражения y")
    print("3. Вычисление суммы ряда S")
    
    choice = input_module.get_user_choice()
    
    if choice == 1:
        x = input_module.get_float_input("Введите значение x: ")
        result = processing_module.calculate_z(x)
        output_module.display_result("Результат z:", result)
    elif choice == 2:
        x = input_module.get_float_input("Введите значение x: ")
        result = processing_module.calculate_y(x)
        output_module.display_result("Результат y:", result)
    elif choice == 3:
        epsilon = input_module.get_positive_float_input("Введите точность ε: ")
        result = processing_module.calculate_series_sum(epsilon)
        output_module.display_result("Сумма ряда S:", result)
    else:
        print("Неверный выбор задачи.")

if __name__ == "__main__":
    main()