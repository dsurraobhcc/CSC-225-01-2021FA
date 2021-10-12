"""
Source: A Byte of Python, by Swaroop C.H.
https://www.oercommons.org/courses/a-byte-of-python
Chapter: Object Oriented Programming
Class variables and Instance variables
"""

class Robot:
    """Represents a robot, with a name."""
    # A class variable/attribute
    population = 0
    all_robots = []

    def __init__(self, name):
        # An instance variable/attribute
        self.name = name
        print("(Initializing {})".format(self.name))

         # When this person is created, the robot # adds to the population 
        Robot.population += 1
        Robot.all_robots.append(self)

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        Robot.all_robots.remove(self)

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    # https://docs.python.org/3/library/functions.html?highlight=classmethod#classmethod
    # decorators
    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))

    def __str__(self):
        return self.name


if __name__ == '__main__':
    # object (droid1) vs class (Robot)
    droid1 = Robot("R2-D2") 
    Robot.how_many()

    droid2 = Robot("C-3PO") 
    Robot.how_many()

    droid2.die()
    for robot in Robot.all_robots:
        print(robot)

    Robot.how_many()