import main


class Photo:
    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = tags

    def get_orientation(self):
        return self.orientation

    def get_tags(self):
        return self.tags

    def get_nb_tags(self):
        return len(self.tags)


class Slide:
    def __init__(self, photos):
        self.photos = []
        if len(photos) == 1 and photos[0].get_orientation() == 'H':
            self.photos = photos
        elif len(photos) == 2 and photos[0].get_orientation() == photos[1].get_orientation() == 'V':
            self.photos = photos
        else:
            raise ValueError("The slide is wrong!")

    def get_photos(self):
        return self.photos

    def get_type(self):
        return self.photos[0].get_orientation()


lines = main.get_non_empty_lines("assignment/a_example.txt")
photos = []
nb_photos = int(lines[0])
for i, line in enumerate(lines[1:]):
    infos = line.split(' ')
    photos.append(Photo(i, infos[0], infos[2:]))

print('')
