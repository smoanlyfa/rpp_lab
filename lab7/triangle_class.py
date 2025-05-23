class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, a, b, c):
        #проверка типа данных
        if not all(isinstance(side, (int, float)) for side in [a, b, c]):
            raise IncorrectTriangleSides("Стороны должны быть числами")
        #проверка на положительные числа
        if not all(side > 0 for side in [a, b, c]):
            raise IncorrectTriangleSides("Стороны должны быть положительными числами")
        #проверка существования треугольника
        if (a + b <= c) or (a + c <= b) or (b + c) <= a:
            raise IncorrectTriangleSides("Недопустимые стороны для треугольника")
        self.a = a
        self.b = b
        self.c = c

#определение треугольника
    def triangle_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "nonequilateral"
#периметр
    def perimeter(self):
        return self.a + self.b + self.c
    
