class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        # input validation
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Odometer reading cannot be rolled back!')

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You can\'t roll back an odometer!')

    def fill_gas_tank(self):
        print("Filling gas tank...")


class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(75)

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


if __name__ == '__main__':
    # my_new_car = Car('audi', 'a4', 2019)
    # print(my_new_car.get_descriptive_name())
    # my_new_car.read_odometer()

    # my_new_car.odometer_reading = 23
    # my_new_car.read_odometer()

    # my_new_car.update_odometer(10)
    # my_new_car.read_odometer()

    # my_new_car.increment_odometer(100)
    # my_new_car.read_odometer()

    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()