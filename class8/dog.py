"""
Define a Dog class with attributes name and age
Define a constructor method for the class
"""

# CamelCase
class Dog:

    # create attributes in the constructor
    def __init__(self, name, age):
        self.name = name # self.name is an instance variable
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")


if __name__ == '__main__':
    my_dog = Dog('Willie', 6) # calling the constructor
    your_dog = Dog('Lucy', 3)

    print(f"My dog's name is {my_dog.name}, age {my_dog.age}")
    print(f"Your dog's name is {your_dog.name}, age {your_dog.age}")

    my_dog.sit()
    your_dog.roll_over()
