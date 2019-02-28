import main


class Photo:
    def __init__(self, orientation, tags):
        self.orientation = orientation
        self.tags = tags

    def get_orientation(self):
        return self.orientation

    def get_tags(self):
        return self.tags

    def get_nb_tags(self):
        return len(self.tags)


lines = main.get_non_empty_lines("assignment/a_example.txt")
photos = []
nb_photos = int(lines[0])
for line in lines[1:]:
    infos = line.split(' ')
    photos.append(Photo(infos[0], infos[2:]))

print('')
