import math


class Rectangle:
    def __init__(self, topleft, xlength, ylength):
        if (isinstance(topleft, list) and len(topleft) == 2 and
                isinstance(xlength, (int, float)) and xlength > 0 and
                isinstance(ylength, (int, float)) and ylength > 0):
            self.topleft = topleft
            self.xlength = xlength
            self.ylength = ylength
            print("Rectangle object created successfully.")
        else:
            print("Specified rectangle cannot be created!!!")
            self.topleft = None
            self.xlength = None
            self.ylength = None

    def intersect(self, other):
        return (self.topleft[0] < other.topleft[0] + other.xlength and
                self.topleft[0] + self.xlength > other.topleft[0] and
                self.topleft[1] < other.topleft[1] + other.ylength and
                self.topleft[1] + self.ylength > other.topleft[1])
    def area(self):
        return self.xlength * self.ylength

    def __lt__(self, other):
        return self.area() < other.area()

    def center(self):
        center_x = self.topleft[0] + self.xlength / 2
        center_y = self.topleft[1] + self.ylength / 2
        return center_x, center_y

    def distance(self, other):
        x1, y1 = self.center()
        x2, y2 = other.center()
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def generate_adjacent(self, side):
        if side == 'right':
            adjacent_topleft = [self.topleft[0] + self.xlength, self.topleft[1]]
        elif side == 'left':
            adjacent_topleft = [self.topleft[0] - self.xlength, self.topleft[1]]
        elif side == 'above':
            adjacent_topleft = [self.topleft[0], self.topleft[1] + self.ylength]
        elif side == 'below':
            adjacent_topleft = [self.topleft[0], self.topleft[1] - self.ylength]
        else:
            print("Invalid side parameter! Only 'right', 'left', 'above', or 'below' are allowed.")
            return None

        return Rectangle(adjacent_topleft, self.xlength, self.ylength)

