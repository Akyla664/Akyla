#Акулов Артём, вариант №4, практичка № 20, основная программа
import vector_operations as vo


if __name__ == "__main__":
   
    vector1 = [3, 4, 5]
    vector2 = [1, 2, 3]

    
    result_add = vo.add_vectors(vector1, vector2)
    print(f"Сложение векторов: {result_add}")

    
    result_sub = vo.subtract_vectors(vector1, vector2)
    print(f"Вычитание векторов: {result_sub}")

    
    result_dot = vo.dot_product(vector1, vector2)
    print(f"Скалярное умножение: {result_dot}")

    
    scalar = 2
    result_mul = vo.multiply_vector_by_scalar(vector1, scalar)
    print(f"Умножение вектора на число {scalar}: {result_mul}")

    
    length = vo.vector_length(vector1)
    print(f"Длина вектора {vector1}: {length}")
