import math

class Rectangle:
    def __init__(self, topleft, xlength, ylength):
        # 1. For valid xlength, ylength, and topleft parameters, the rectangle object is created.
        if isinstance(topleft, list) and len(topleft) == 2 and isinstance(xlength, (int, float)) and isinstance(ylength, (int, float)):
            self.topleft = topleft
            self.xlength = xlength
            self.ylength = ylength
            print("Rectangle object created successfully.")
        else:
            print("Specified rectangle cannot be created!!!")
            # 2. If xlength or ylength is 0 or negative, set attributes to None
            self.topleft = None
            self.xlength = None
            self.ylength = None

##
    def intersect(self, other):
        # Check if self intersects with other rectangle
        if (self.topleft[0] < other.topleft[0] + other.xlength and
                self.topleft[0] + self.xlength > other.topleft[0] and
                self.topleft[1] < other.topleft[1] + other.ylength and
                self.topleft[1] + self.ylength > other.topleft[1]):
            return True
        else:
            return False

##
    def area(self):
        return self.xlength * self.ylength

    def __lt__(self, other):
        # Check if area of self rectangle is less than area of other rectangle
        return self.area() < other.area()

##
    def center(self):
        # Calculate center coordinates
        center_x = self.topleft[0] + self.xlength / 2
        center_y = self.topleft[1] + self.ylength / 2
        return center_x, center_y

    def distance(self, other):
        # Calculate Euclidean distance between centers of two rectangles
        x1, y1 = self.center()
        x2, y2 = other.center()
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#

    def generate_adjacent(self, side):
        # Calculate dimensions of adjacent rectangle
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

        # Create and return adjacent rectangle
        return Rectangle(adjacent_topleft, self.xlength, self.ylength)
# Örnek kullanım:
# rectangle = Rectangle([2, 3], 4, 5)
