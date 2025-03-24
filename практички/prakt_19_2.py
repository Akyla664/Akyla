#Акулов Артём, вариант №4, практичка № 19, Модуль для обработки
import math

def calculate_z(x):
    # Вычисление выражения z
    numerator = math.cos(x)
    denominator = (math.sin(x))**2 + 5
    term1 = numerator / denominator
    term2 = math.exp(x**2)
    term3 = 4.48 * 10**(-1)
    return term1 - term2 + term3

def calculate_y(x):
    # Вычисление выражения y
    a = 10
    term1 = math.sqrt(a * x) / math.sin(math.log(x))
    term2 = math.sqrt(math.cos(x**2) / x**2)
    return term1 - term2

def calculate_series_sum(epsilon):
    # Вычисление суммы ряда S = Σ(1/(i*(i+1))) с точностью ε
    i = 1
    total_sum = 0
    current_term = 1 / (i * (i + 1))
    
    while abs(current_term) >= epsilon:
        total_sum += current_term
        i += 1
        current_term = 1 / (i * (i + 1))
    
    return total_sum