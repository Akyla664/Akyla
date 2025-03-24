#Акулов Артём, вариант №4, практичка № 17

def input_array(prompt, size):
    print(prompt)
    return [int(input(f"Введите элемент {i + 1}: ")) for i in range(size)]


def print_array(array, message="Массив:"):
    print(message, array)


def append_to_array(array, value):
    array.append(value)


def remove_element_by_index(array, index):
    if 0 <= index < len(array):
        array.pop(index)


def insert_at_start(array, value):
    array.insert(0, value)


def merge_arrays(array1, array2):
    return array1 + array2


def sort_descending(array):
    return sorted(array, reverse=True)

def filter_by_index_multiple_of_3(array):
    return [array[i] for i in range(len(array)) if i % 3 == 0]


def shift_left(array):
    if len(array) > 1:
        first_element = array[0]
        array = array[1:] + [first_element]
    return array


if __name__ == "__main__":
   
    E = input_array("Введите 7 элементов массива E:", 7)
    F = input_array("Введите 8 элементов массива F:", 8)

   
    append_to_array(E, 88)  
    print_array(E, "Массив E после добавления 88:")

    remove_element_by_index(E, 1) 
    print_array(E, "Массив E после удаления второго элемента:")

    
    insert_at_start(F, 11)  
    print_array(F, "Массив F после вставки 11 в начало:")

    
    EF1 = merge_arrays(E, F) 
    print_array(EF1, "Массив EF1 после объединения E и F:")

    EF1 = sort_descending(EF1)  
    print_array(EF1, "Массив EF1 после сортировки по убыванию:")

  
    EF2 = filter_by_index_multiple_of_3(EF1) 
    print_array(EF2, "Массив EF2 (элементы с индексами, кратными 3):")

    EF2 = shift_left(EF2)
    print_array(EF2, "Массив EF2 после сдвига влево на 1 позицию:")