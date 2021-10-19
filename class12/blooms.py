'''
class exercise
'''
import math

class Flower:

    def __init__(self, label, x, y, radius):
        self.label = label
        self.x = x
        self.y = y
        self.radius = radius

    def causes_bloom(self, other):
        # self causes other to bloom if the distance
        # between the centers is less than the radius of self
        distance = math.sqrt(
            (self.x - other.x)**2 + (self.y - other.y)**2)
        print(f'distance: {distance}')
        print(f'radius: {self.radius}')

        if distance <= self.radius:
            return True
        else:
            return False


if __name__ == '__main__':
    b = Flower("B", 6.5, 17, 7)
    a = Flower("A", 7, 13, 3)
    g = Flower("G", 8.5, 11.5, 3)
    flowers = [b, a, g]

    # print(b.causes_bloom(a)) # True
    # print(a.causes_bloom(b)) # False
    # print(g.causes_bloom(a))
    # print(a.causes_bloom(g))

    print(a.causes_bloom(b))