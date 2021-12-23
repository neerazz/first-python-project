from math import sqrt


class Line:

    def __init__(self, cor1, cor2):
        self.cor1 = cor1
        self.cor2 = cor2

    def dist(self):
        x1, y1 = self.cor1
        x2, y2 = self.cor2
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def slope(self):
        x1, y1 = self.cor1
        x2, y2 = self.cor2
        return (y2 - y1) / (x2 - x1)
