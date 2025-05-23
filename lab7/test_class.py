import pytest
from triangle_class import Triangle, IncorrectTriangleSides

#ПОЗИТИВНЫЕ ТЕСТЫ

#равносторонний треугольник
def test_equilateralal():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 9

#равнобедренный треугольник
def test_isosceles():
    t1 = Triangle(3, 4, 4)
    t2 = Triangle(4, 3, 4)
    t3 = Triangle(4, 4, 3)
    assert t1.triangle_type() == "isosceles"
    assert t2.triangle_type() == "isosceles"
    assert t3.triangle_type() == "isosceles"
    assert t1.perimeter() == 11

#разносторонний треугольник
def test_nonequilateral():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12

#НЕГАТИВНЫЕ ТЕСТЫ

#отрицательное число 
def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 4, 5)

#проверка на ноль
def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 4, 5)

#проверка на число (тип данных)
def test_non_number():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("a", 4, 5)

#несуществующий треугольник
def test_no_triangle():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)

