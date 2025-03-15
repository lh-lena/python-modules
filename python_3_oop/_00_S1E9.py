"""_summary_
Create an abstract class "character" which can take a first_name as first parameter,
is_alive as second non mandatory parameter set to True by default and can change the
health state of the character with a method that passes is_alive from True to False.
And a "stark" class which inherits from Character
"""

# Python program showing
# abstract base class work
from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        super().__init__()

    @abstractmethod
    def die(self):
        """Your docstring for Method"""
        pass


class Stark(Character):
    """Your docstring for Class"""
    def die(self) -> bool:
        """Your docstring for Method"""
        if self.is_alive == True:
            self.is_alive = False
        return self.is_alive

