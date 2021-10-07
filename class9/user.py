class User():

    def __init__(self, firstname, lastname, email=None):
        self.firstname = firstname.title()
        self.lastname = lastname.title()

    # define special method
    def __str__(self):
        return 'This user is ' + self.firstname + ' ' + self.lastname

    def describe_user(self):
        print(self.firstname + ' ' + self.lastname)

    def greet_user(self):
        print("Hello " + self.firstname + ' ' + self.lastname)

if __name__ == '__main__':
    user1 = User('dominic', 'surrao')
    # user1.describe_user()
    # user1.greet_user()

    print(user1)