import main

lines = main.get_non_empty_lines("assignment/a_example.txt")


class Photo:
    def __init__(self, orientation, tags):
        self.orientation = orientation
        self.tags = tags

    def get_orientation(self):
        return self.orientation

    def get_tags(self):
        return self.tags
