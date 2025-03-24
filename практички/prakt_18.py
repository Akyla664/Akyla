#Акулов Артём, вариант №4, практичка № 18

def f(x):
  
    return x**2 - 4


def Root(a, b, e):
    """
    Находит корень уравнения f(x) = 0 методом деления отрезка пополам.
    
    :param a: Левая граница интервала [a, b].
    :param b: Правая граница интервала [a, b].
    :param e: Точность вычисления корня.
    :return: Приближенное значение корня с точностью e.
    """
   
    c = (a + b) / 2
    
    
    if abs(b - a) < e:
        return c
    
    
    if f(a) * f(c) < 0:
       
        return Root(a, c, e)
    else:
   
        return Root(c, b, e)


if __name__ == "__main__":
   
    a = 1  
    b = 3  
    e = 1e-6  

  
    if f(a) * f(b) >= 0:
        print("Условие f(a) * f(b) < 0 не выполняется. Метод не применим.")
    else:
        
        root = Root(a, b, e)
        print(f"Корень уравнения: {root}")