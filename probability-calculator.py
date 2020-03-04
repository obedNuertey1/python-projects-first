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

    def __get_new_entries(self):
        # Recalculate the `entries` dictionary to reflect the current state of `contents`.
        new_dict = {key: 0 for key, value in self.entries.items()}  # Initialize all counts to zero.
        for item in self.contents:
            new_dict[item] += 1  # Count occurrences of each ball color in `contents`.
        self.entries = new_dict  # Update the entries to reflect current state.
    
    def __str__(self):
        # Custom string representation for debugging or printing the Hat object.
