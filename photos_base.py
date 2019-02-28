def get_non_empty_lines(filename):
    try:
        lines = [line.strip() for line in open(filename, "r")]
        lines = [line for line in lines if line]  # Skipping blank lines
        return lines
    except IOError as e:
        print("Unable to read output file!\n" + e)
        return []


class Photo:
    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = tags
        self.hasBeenUsed = False

    def get_orientation(self):
        return self.orientation

    def get_tags(self):
        return self.tags

    def get_nb_tags(self):
        return len(self.tags)

    def get_id(self):
        return self.id

    def set_has_been_used(self):
        self.hasBeenUsed = True


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

    def __str__(self):
        return '{}'.format(self.photos[0].get_id()) if self.get_type() == 'H' else '{} {}'.format(
            self.photos[0].get_id(), self.photos[1].get_id())


# def algo_nul(photos):
#     for photo in photos:


lines = get_non_empty_lines("assignment/a_example.txt")
photos = []
nb_photos = int(lines[0])
for i, line in enumerate(lines[1:]):
    infos = line.split(' ')
    photos.append(Photo(i, infos[0], infos[2:]))

print(Slide([photos[0]]))
