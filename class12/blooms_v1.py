class Flower:
    def __init__(self, name = "", x = 0, y = 0):
        self.name = name
        self.x = x
        self.y = y
        self.radius = 0
        self.is_blooming = False
        self.flowers_bloomed = 0

    def bloom(self):
        if self.is_blooming is False:
        self.is_blooming = True
  
    def make_bloom(self, factor):
        if self.is_blooming:
        self.radius = self.radius + (0.1 * factor)

    def detect_collision(self, other_flower):
        # working