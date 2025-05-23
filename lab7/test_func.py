import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestGetTriangleType(unittest.TestCase):

#ПОЗИТИВНЫЕ ТЕСТЫ
#равносторонний треугольник
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")

#равнобедренный треугольник
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(3, 4, 4), "isosceles")
        self.assertEqual(get_triangle_type(4, 3, 4), "isosceles")
        self.assertEqual(get_triangle_type(4, 4, 3), "isosceles")

#разносторонний треугольник
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

#НЕГАТИВНЫЕ ТЕСТЫ

#отрицательное число  
    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 4, 5)
    
#проверка на ноль
    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)

#проверка на число (тип данных)
    def test_non_number(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 4, 5)

#несуществующий треугольник
    def test_no_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)


if __name__ == '__main__':
    unittest.main()

        