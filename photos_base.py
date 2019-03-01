import random


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
        self.tags = set(tags)
        self.hasBeenUsed = False

    def get_orientation(self):
        return self.orientation

    def get_tags(self):
        return self.tags

    def get_nb_tags(self):
        return len(self.tags)

    def get_id(self):
        return self.id


class Slide:
    def __init__(self, photos):
        if len(photos) == 1 and photos[0].get_orientation() == 'H':
            self.photos = photos
            self.tags = photos[0].get_tags()
        elif len(photos) == 2 and photos[0].get_orientation() == photos[1].get_orientation() == 'V':
            self.photos = photos
            self.tags = photos[0].get_tags() | photos[1].get_tags()
        else:
            raise ValueError("The slide is wrong!")

    def get_tags(self):
        return self.tags

    def get_type(self):
        return self.photos[0].get_orientation()

    def __str__(self):
        return '{}'.format(self.photos[0].get_id()) if self.get_type() == 'H' else '{} {}'.format(
            self.photos[0].get_id(), self.photos[1].get_id())


def make_pairs(vertical_photos):
    available_pairs = [list() for i in range(int(len(vertical_photos) / 2))]
    finished_pairs = []
    unused_photos = list(vertical_photos)
    for photo in vertical_photos:
        finished = False
        for pair in available_pairs:
            if len(pair) == 0 or len(pair[0].get_tags() & photo.get_tags()) == 0:
                pair.append(photo)
                if len(pair) == 2:
                    finished_pairs.append(Slide(pair))
                    finished = True
                unused_photos.remove(photo)
                break

        if finished:
            available_pairs.remove(finished_pairs[-1].photos)
    for i, photo in enumerate(unused_photos):
        pair = available_pairs[random.randrange(len(unused_photos) - i)]
        pair.append(photo)
        finished_pairs.append(Slide(pair))
        available_pairs.remove(pair)

    return finished_pairs


def algo_eclate_au_sol(file):
    def interest_factor(slide_1, slide_2, bound):
        tags_1 = slide_1.get_tags()
        tags_2 = slide_2.get_tags()

        in_both = len(tags_1 & tags_2)
        if in_both < bound:
            return in_both
        one_but_not_two = len(tags_1 - tags_2)
        if one_but_not_two < bound:
            return one_but_not_two
        two_but_not_one = len(tags_2 - tags_1)

        return min(one_but_not_two, two_but_not_one, in_both)

    photos = parse_file(file)
    v_photos = []
    h_slides = []
    for photo in photos:
        if photo.get_orientation() == 'V':
            v_photos.append(photo)
        else:
            h_slides.append(Slide([photo]))

    v_slides = make_pairs(v_photos)

    slides = v_slides + h_slides

    slides = sorted(slides, reverse=True, key=lambda kv: len(kv.get_tags()))

    new_slides = [slides[0]]
    del slides[0]

    for i in range(len(slides)):
        best_slide = slides[0]
        index = 0
        max_score = interest_factor(new_slides[-1], best_slide, 0)
        for j, slide in enumerate(slides[1:len(slides)]):
            score = interest_factor(new_slides[-1], slide, max_score)
            if score > max_score:
                best_slide = slide
                index = j + 1
                max_score = score
        new_slides.append(best_slide)
        del slides[index]

    print(len(new_slides))
    for i in range(0, len(new_slides)):
        print(new_slides[i])


def parse_file(file):
    lines = get_non_empty_lines(file)
    photos = []
    for i, line in enumerate(lines[1:]):
        infos = line.split(' ')
        photos.append(Photo(i, infos[0], infos[2:]))
    return photos


# FAITES VOS TESTS ICI SI BESOIN
if __name__ == "__main__":
    print()
