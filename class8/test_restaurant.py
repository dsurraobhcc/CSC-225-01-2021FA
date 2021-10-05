# import definitions from the 'restaurant' module
from restaurant import Restaurant, IceCreamStand

if __name__ == '__main__':
    my_restaurant = Restaurant('The Greasy Spoon', 'Breakfast') #variable holding an instance of the Dog class
    your_restaurant = Restaurant('Alfredos', 'Italian')

    my_restaurant.describe_restaurant()
    your_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()

    jp_licks = IceCreamStand('JP Licks', 'Ice cream',
        ['Chocolate', 'Vanilla', 'Double Chocolate'])
    jp_licks.describe_restaurant()
    jp_licks.open_restaurant()

    jp_licks.add_flavors(['Strawberry', 'Pistachio', 'Cotton Candy', 'Chocolate'])
    jp_licks.describe_restaurant()

    # how do you avoid duplicate flavors?