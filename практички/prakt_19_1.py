#Акулов Артём, вариант №4, практичка № 19, Модуль для ввода данных
import math

def get_user_choice():
    while True:
        try:
            choice = int(input("Введите номер задачи (1-3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Неверный выбор. Пожалуйста, введите число от 1 до 3.")
        except ValueError:
            print("Ошибка: Введите целое число.")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Введите действительное число.")

def get_positive_float_input(prompt):
    while True:
        value = get_float_input(prompt)
        if value > 0:
            return value
        else:
            print("Ошибка: Введите положительное число.")