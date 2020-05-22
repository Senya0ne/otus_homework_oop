from code.Figure import Figure


class Triangle(Figure):

    def __init__(self, name):
        super().__init__(name)

    def get_area(self, a, h):
        super().get_area()
        s = 0.5 *(a*h)
        return f'Площадь {self.name}а равна ' + str(s)

    def get_angles(self, angles):
        pass

    def get_perimeter(self, perimeter):
        pass


triangle = Triangle('Треугольник')
print(triangle.name)

a = triangle.get_area(1, 5)
print(a)
