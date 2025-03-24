#Акулов Артём, вариант №4, практичка № 20, модуль действий с векторами
import math

def add_vectors(v1, v2):
    """
    Сложение двух векторов.
    
    :param v1: Первый вектор (список чисел).
    :param v2: Второй вектор (список чисел).
    :return: Результат сложения векторов (список чисел).
    """
    if len(v1) != len(v2):
        raise ValueError("Векторы должны иметь одинаковую длину.")
    return [x + y for x, y in zip(v1, v2)]

def subtract_vectors(v1, v2):
    """
    Вычитание второго вектора из первого.
    
    :param v1: Первый вектор (список чисел).
    :param v2: Второй вектор (список чисел).
    :return: Результат вычитания векторов (список чисел).
    """
    if len(v1) != len(v2):
        raise ValueError("Векторы должны иметь одинаковую длину.")
    return [x - y for x, y in zip(v1, v2)]

def dot_product(v1, v2):
    """
    Скалярное умножение двух векторов.
    
    :param v1: Первый вектор (список чисел).
    :param v2: Второй вектор (список чисел).
    :return: Результат скалярного умножения (число).
    """
    if len(v1) != len(v2):
        raise ValueError("Векторы должны иметь одинаковую длину.")
    return sum(x * y for x, y in zip(v1, v2))

def multiply_vector_by_scalar(v, scalar):
    """
    Умножение вектора на число.
    
    :param v: Вектор (список чисел).
    :param scalar: Число для умножения.
    :return: Результат умножения вектора на число (список чисел).
    """
    return [x * scalar for x in v]

def vector_length(v):
    """
    Определение длины вектора.
    
    :param v: Вектор (список чисел).
    :return: Длина вектора (число).
    """
    return math.sqrt(sum(x**2 for x in v))