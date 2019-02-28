import random

import main

lines = main.get_non_empty_lines("pizza-stuff/a_example.in")
corner = (0, 0, 0, 0)
probs = [0, 0.5, 0, 0.5]  # top, bottom, left, right


# First strategy: biggest possible slice with at least L of each
# Parameters: starting corner / exploration direction probabilities

def explore_top(pizza_slice):
    return pizza_slice[0] - 1, pizza_slice[1], pizza_slice[2], pizza_slice[3]


def explore_bottom(pizza_slice):
    return pizza_slice[0], pizza_slice[1], pizza_slice[2] + 1, pizza_slice[3]


def explore_left(pizza_slice):
    return pizza_slice[0], pizza_slice[1] - 1, pizza_slice[2], pizza_slice[3]


def explore_right(pizza_slice):
    return pizza_slice[0], pizza_slice[1], pizza_slice[2], pizza_slice[3] + 1


class Pizza:
    def __init__(self, pizza_lines):
        parameters = pizza_lines[0].split(' ')
        self.rows = int(parameters[0])
        self.columns = int(parameters[1])
        self.min_ing = int(parameters[2])
        self.max_cells = int(parameters[3])
        self.cells = pizza_lines[1:]

    def get_slice(self, x1, y1, x2, y2):
        if x1 < 0 or x2 >= self.rows or y1 < 0 or y2 >= self.columns or x1 > x2 or y1 > y2:
            raise ValueError("Impossible slicing: {} {} {} {}".format(x1, y1, x2, y2))
        tomatoes = 0
        mushrooms = 0
        for line in lines[x1:(x2 + 1)]:
            for ingredient in line[y1:(y2 + 1)]:
                if ingredient == 'T':
                    tomatoes += 1
                else:
                    mushrooms += 1
        return tomatoes, mushrooms, (x2 - x1) * (y2 - y1)

    def get_slice_from_tuple(self, pizza_slice):
        return self.get_slice(pizza_slice[0], pizza_slice[1], pizza_slice[2], pizza_slice[3])

    def explore(self, pizza_slice, probs):
        new_slice = tuple(pizza_slice)
        rnd_val = random.uniform(0, 1)
        choice = -1
        if rnd_val <= probs[0] and new_slice[0] > 0:
            new_slice = explore_top(new_slice)
            choice = 0
        elif rnd_val <= probs[0] + probs[1] and new_slice[2] < self.rows:
            new_slice = explore_bottom(new_slice)
            choice = 1
        elif rnd_val <= 1 - probs[3] and new_slice[1] > 0:
            new_slice = explore_left(new_slice)
            choice = 2
        elif rnd_val <= 1 and new_slice[3] < self.columns:
            new_slice = explore_right(new_slice)
            choice = 3

        return new_slice, self.get_slice_from_tuple(new_slice), choice

# Won't work because backtracking with random choices is not really something
# def slicer(pizza, corner, probs):
#     current_slice = corner
#     satisfies = False
#
#     # loop
#     prev_slice = tuple(current_slice)
#     current_slice, slice_stats, action = pizza.explore(current_slice, probs)
#
#     if prev_slice == current_slice:
#         if satisfies:
#             return current_slice
#
#     if slice_stats[0] > pizza.min_ing and slice_stats[1] > pizza.min_ing:
#         satisfies = True
#
#     if slice_stats[3] > pizza.max_cells:
#         current_slice = prev_slice
#         probs[action] = 0
#         for i, prob in enumerate(probs):
#             if prob > 0:
#                 probs[i] = 1
#     # check if satisfies or violates properties
#     # if same see for backtrack or stop idk
#
#     return something


# if __name__ == "__main__":
#     slicer(Pizza(lines), corner, probs)
