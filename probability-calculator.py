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
        self.__get_new_entries()  # Ensure entries are up to date.
        entries = tuple(f'{val}={key}' for val, key in self.entries.items())  # Format entries as strings.
        return f'{self.__class__.__name__}{str(entries)}'

    def __repr__(self):
        # Representation method for debugging purposes.
        self.__get_new_entries()  # Ensure entries are up to date.
        entries = tuple(f'{val}={key}' for val, key in self.entries.items())  # Format entries as strings.
        return f'{self.__class__.__name__}{str(entries)}'
    
    def draw(self, n_balls):
        # Draw `n_balls` randomly from the hat.
        if n_balls > len(self.contents):
            # If requested number exceeds available balls, return all balls.
            drawn = copy.deepcopy(self.contents)
            self.contents = []
            return drawn
        
        balls_drawn = []  # List to store drawn balls.
        contents = copy.deepcopy(self.contents)  # Deep copy to prevent modifying original list.
        
        for i in range(n_balls):
            rand_index = random.randint(0, len(contents) - 1)  # Get a random index.
            balls_drawn.append(contents[rand_index])  # Add the ball at the random index to the result.
            contents.pop(rand_index)  # Remove the ball from the contents list.
        
        self.contents = contents  # Update the original contents after drawing.

        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    def _is_subset(drawn, expected):
        for color, count in expected.items():
            if drawn.get(color, 0) < count:
                return False
        return True

    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_dict = {}
        for ball in drawn_balls:
            drawn_dict[ball] = drawn_dict.get(ball, 0) + 1

        if _is_subset(drawn_dict, expected_balls):
            success_count += 1

    return success_count / num_experiments

