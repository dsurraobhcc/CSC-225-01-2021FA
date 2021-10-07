class Restaurant:

    #create attributes in the constructor    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name #self.name is an instance variable
        self.cuisine_type = cuisine_type

    # Define methods:
    def describe_restaurant(self):
        """
        Print out the restaurant name and cuisine type
        """
        print("The restaurant name is " + self.restaurant_name 
            + " serving " + self.cuisine_type + " cuisine")

    def open_restaurant(self):
        """
        Opens the restaurant now!
        """
        print(f"{self.restaurant_name} is open!")           

# CLASS INHERITANCE
# Make IceCreamStand a subclass of Restaurant
# The class IceCreamStand inherits from Restaurant
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        # call the parent's constructor
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    # overriding the method
    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name 
            + " serving flavors " + ', '.join(self.flavors))

    def add_flavors(self, flavors=[]):
        """
        Add new flavors to existing list
        """
        # add a check for duplicate flavors
        
        # for flavor in flavors:
        #     if flavor not in self.flavors:
        #         self.flavors.append(flavor)

        self.flavors += flavors
        self.flavors = list(set(self.flavors))


