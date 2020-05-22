class Figure:

    def __init__(self, name):
        self.name = name

    def get_area(self):
        return f'Площадь {self.name} равна'

    def get_angles(self, angles):
        return f'Количество углов у фигуры - ' + angles

    def get_perimeter(self, perimeter):
        return f'Периметр фигуры равен' + perimeter


