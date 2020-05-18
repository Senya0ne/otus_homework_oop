class Figure:

    def __init__(self, name):
        self.name = name

    def get_area(self):
        return f'Площадь {self.name} равна'

    def get_angles(self, angles):
        return f'Количество углов у фигуры - ' + angles

    def get_perimeter(self, perimeter):
        return f'Периметр фигуры равен' + perimeter


class Triangle(Figure):

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def get_area(self, a, h):
        super().get_area()
        area = 0.5 * (a * h)
        return f'Площадь {self.name} равна ' + str(area)

    def get_angles(self, angles):
        pass

    def get_perimeter(self, perimeter):
        pass


#
# class Rectangle(Figure):
#     pass
#
# class Square(Figure):
#     pass
#
# class Circle(Figure):
#     pass

triangle = Triangle('Треугольник')
print(triangle.name)

a = triangle.get_area(1, 5)
print(a)
