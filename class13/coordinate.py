import math
'''
2-dimensional coordinate (x, y) 
'''

class Coordinate():

    # constructor
    def __init__(self, x, y):
        self.x = x # instance variable
        self.y = y

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    # special method: override
    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == '__main__':
    origin = Coordinate(0, 0) # object: instance of Coordinate class
    point2 = Coordinate(3, 4)
    point3 = Coordinate(3, 4)

    print(origin, point2, point3)

    print(origin == point2)
    print(point2 == point3)
