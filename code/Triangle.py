from code.Figure import Figure


class Triangle(Figure):

    def __init__(self, name, angles):
        super().__init__(name, angles)

    def get_area(self, a, h):
        s = 0.5 * (a*h)
        return f'Площадь {self.name}а равна ' + str(s)

    def get_angles(self, angles):
        return f'Количество углов равно ' + str(self.angles)

    def get_perimeter(self, perimeter):
        super().get_perimeter()
        return f'Периметр {self.name}а равна ' + str(p)


triangle = Triangle('Треугольник', 3)
print(triangle.name, triangle.get_angles(3))

a = triangle.get_area(1, 5)
print(a)
