import copy
import random
from inspect import signature

class Hat:
    def __init__(self, **kwargs):
        # Initialize the Hat object with keyword arguments representing colors and their counts.
        self.entries = kwargs  # Dictionary of color names as keys and their counts as values.
        self.contents = []  # List to store all balls by color.

        # Populate the contents list with balls based on their counts.
        for value, key in self.entries.items():
            temp = [value for i in range(key)]  # Create a list of `value` repeated `key` times.
            self.contents += temp  # Add these balls to the contents list.

