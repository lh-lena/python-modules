"""
Create two families that inherit from the Character class, that we can instantiate
without going through the Character class. Find a solution so that "__str__" and
"__repr__" return strings and not objects.
Write a Class method to create characters in a chain.

https://python-course.eu/oop/object-oriented-programming.php
https://docs.python.org/2/library/functions.html#super

"""

from _00_S1E9 import Character

class Baratheon(Character):
    #your code here
    """Representing the Baratheon family."""
    def __init__(self, firt_name: str):
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
        super().__init__(firt_name)

    def __str__(self):
        return f"{type(self)} ('{self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self):
        return f"{type(self)} ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        if self.is_alive:
            self.is_alive = False
        return self.is_alive

class Lannister(Character):
    #your code here
    """Representing the Lannister family."""

    def __init__(self, firt_name: str):
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
        super().__init__(firt_name)

    def __str__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repl__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

        # decorator
        # def create_lannister(your code here):
    def die(self):
        if self.is_alive:
            self.is_alive = False
        return self.is_alive