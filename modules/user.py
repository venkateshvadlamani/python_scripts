"""Typical User object used in various projects

variables: first_name, last_name, email, phone_number, userid
"""


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_variables(self):
        print(self.first_name)
        print(self.last_name)