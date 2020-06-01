class Figure:
    angles = None

    def __init__(self, name, angles):
        self.perimeter = None
        self.area = None
        self.name = name
        self.angles = angles

    def get_area(self):
        return f'Площадь {self.name} равна' + self.area

    def get_angles(self, angles):
        return f'Количество углов у фигуры - ' + self.angles

    def get_perimeter(self, perimeter):
        return f'Периметр фигуры равен' + self.perimeter
