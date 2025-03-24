#Акулов Артём, вариант №4, практичка № 16

def sum_less_than(numbers, threshold):
    """
    Возвращает сумму элементов списка, значения которых меньше заданного порога.

    :param numbers: Список чисел.
    :param threshold: Пороговое значение (znach).
    :return: Сумма элементов, меньших порогового значения.
    """
    return sum(num for num in numbers if num < threshold)