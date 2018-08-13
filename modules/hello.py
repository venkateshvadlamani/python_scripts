import pprint


# function
def world():
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint('Hello World')


# Define varaible
shark = "Sammy"


# Class
class Octopus:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def tell_me_about_octopus(self):
        print("This octopus is " + self.color + " in color.")
        print(self.name + " is its name.")