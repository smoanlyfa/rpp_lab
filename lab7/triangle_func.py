class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(a, b, c):
#проверка типа данных
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise IncorrectTriangleSides("Стороны должны быть числами")
#проверка на положительные числа
    if not all(side > 0 for side in [a, b, c]):
        raise IncorrectTriangleSides("Стороны должны быть положительными числами")
#проверка существования треугольника
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise IncorrectTriangleSides("Недопустимые стороны для треугольника")
    
#определение треугольника
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"
    
