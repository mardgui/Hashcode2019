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

    def has_been_used(self):
        return self.hasBeenUsed

    def set_has_been_used(self):
        self.hasBeenUsed = True

    def set_has_not_been_used(self):
        self.hasBeenUsed = False

class Photo_v2(Photo):
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

    def set_has_been_used(self):
        self.hasBeenUsed = True

class Slide:
    def __init__(self, photos):
        self.photos = []
        self.has_been_used = False
        if len(photos) == 1 and photos[0].get_orientation() == 'H':
            self.photos = photos
        elif len(photos) == 2 and photos[0].get_orientation() == photos[1].get_orientation() == 'V':
            self.photos = photos
        else:
            raise ValueError("The slide is wrong!")

    def get_tags(self):
        tags = []
        photos = self.photos
        if len(photos) == 1:
            tags.append(photos[0].get_tags())
        if len(photos) == 2:
            tags.append(photos[0].get_tags())
            tags.append(photos[1].get_tags())
        return tags

    def set_has_been_used(self):
        photos = self.photos
        self.has_been_used = True
        if len(photos) == 1:
            photos[0].set_has_been_used()
        if len(photos) == 2:
            photos[0].set_has_been_used()
            photos[1].set_has_been_used()

    def set_has_not_been_used(self):
        photos = self.photos
        self.has_been_used = False
        if len(photos) == 1:
            photos[0].set_has_not_been_used()
        if len(photos) == 2:
            photos[0].set_has_not_been_used()
            photos[1].set_has_not_been_used()

    def get_photos(self):
        return self.photos

    def get_type(self):
        return self.photos[0].get_orientation()

    def __str__(self):
        return '{}'.format(self.photos[0].get_id()) if self.get_type() == 'H' else '{} {}'.format(
            self.photos[0].get_id(), self.photos[1].get_id())

    def has_not_been_used(self):
        return self.has_been_used == False

    def has_been_used(self):
        return self.has_been_used == True

def make_pairs(vertical_photos):
    available_pairs = [list() for i in range(int(len(vertical_photos)/2))]
    finished_pairs = []
    unused_photos = list(vertical_photos)
    for photo in vertical_photos:
        for pair in available_pairs:
            if len(pair) == 0 or len(pair[0].get_tags() & photo.get_tags()) == 0:
                pair.append(photo)
                if len(pair) == 2:
                    finished_pairs.append(Slide(pair))
                unused_photos.remove(photo)
                break

        try:
            if len(finished_pairs) > 0:
                available_pairs.remove(finished_pairs[-1].photos)
        except ValueError:
            print('', end='')
    for i, photo in enumerate(unused_photos):
        pair = available_pairs[random.randrange(len(unused_photos) - i)]
        pair.append(photo)
        finished_pairs.append(Slide(pair))
        available_pairs.remove(pair)

    return finished_pairs

def algo_eclate_au_sol(file):
    photos = parseFile_v2(file)
    v_photos = []
    for photo in photos:
        if photo.get_orientation() == 'V':
            v_photos.append(photo)
    make_pairs(v_photos)

def parseFile_v2(file):
    lines = get_non_empty_lines(file)
    photos = []
    for i, line in enumerate(lines[1:]):
        infos = line.split(' ')
        photos.append(Photo_v2(i, infos[0], infos[2:]))
    return photos


def parseFile(file):
    lines = get_non_empty_lines(file)
    photos = []
    for i, line in enumerate(lines[1:]):
        infos = line.split(' ')
        photos.append(Photo(i, infos[0], infos[2:]))
    return photos


def getNumberLabel(photos):
    dico = {}
    for i in range(0, len(photos)):
        for tags in photos[i].get_tags():
            if tags in dico:
                dico[tags] += 1
            else:
                dico[tags] = 1


# def algo_nul(photos):
#     for photo in photos:


def random_algo(photos):

    slides = []
    i = 0
    while i < len(photos):
        if (photos[i]).get_orientation() == "V":
            for j in range(i + 1, len(photos)):
                if (photos[j]).get_orientation() == "V":
                    slides.append(Slide([photos[i], photos[j]]))
                    i = j + 1
                    break
                else:
                    slides.append(Slide([photos[j]]))
        else:
            slides.append(Slide([photos[i]]))
            i = i + 1

    print(len(slides))
    for i in range(0, len(slides)):
        print(slides[i])

def smart_algo(photos):
    horizontal = []
    horizontalSlide = []
    vertical = []
    Slides = []
    for i in range (0, len(photos)):
        if (photos[i]).get_orientation() == "V":
            vertical.append(photos[i])
        else:
            horizontal.append(photos[i])

    verticalSlide = make_pairs(vertical)
    for horizontals in horizontal:
        horizontalSlide.append(Slide([horizontals]))

    Slides.extend(horizontalSlide)
    Slides.extend(verticalSlide)

    SlidesReturn = []

    for x in range(15,3):
        for i in range(0, len(Slides)):
            actualSlide = Slides[i]
            if actualSlide.has_not_been_used():
                for j in range (i+1, len(Slides)):
                    nextSlide = Slides[j]
                    if nextSlide.has_not_been_used():
                        different, common = compare_two_slides(actualSlide, nextSlide)
                        if different >= x and common >= x:
                            SlidesReturn.append(actualSlide)
                            SlidesReturn.append(nextSlide)
                            actualSlide.set_has_been_used()
                            nextSlide.set_has_been_used()
                            break

    for i in range(0, len(Slides)):
        actualSlide = Slides[i]
        if actualSlide.has_not_been_used():
            SlidesReturn.append(actualSlide)

    print(len(SlidesReturn))
    for i in range(0, len(SlidesReturn)):
        print(SlidesReturn[i])


def mergeVertical(vertical):
    getNumberLabel(vertical)
    verticalMerged = []
    for x in range (0,3):
        for i in range (0,len(vertical)):
            if vertical[i].has_been_used() == False:
                for j in range(i+1,min(i+15,len(vertical))):
                    if vertical[j].has_been_used() == False:
                        if compareLabels(vertical[i].get_tags(), vertical[j].get_tags()) == x:
                            vertical[i].set_has_been_used()
                            vertical[j].set_has_been_used()
                            verticalMerged.append(Slide([vertical[i], vertical[j]]))
                            break

    for i in range (0,len(vertical)):
        if vertical[i].has_been_used() == False:
            for j in range(i + 1, len(vertical)):
                if vertical[j].has_been_used() == False:
                    vertical[i].set_has_been_used()
                    vertical[j].set_has_been_used()
                    verticalMerged.append(Slide([vertical[i], vertical[j]]))
                    break

    for slide in verticalMerged:
        slide.set_has_not_been_used()
    return verticalMerged

def compareLabels(labList1, labList2):
    compteur = 0
    for x in labList1:
        if x in labList2:
            compteur += 1

def compare_two_photos(photo1, photo2):
    different = 0
    commun = 0
    tags_photo_1 = photo1.get_tags()
    tags_photo_2 = photo2.get_tags()

    for tag1 in tags_photo_1:
        for tag2 in tags_photo_2:
            if tag1 == tag2:
                commun += 1
            else:
                different += 1

    return different, commun


def compare_two_slides(slide1, slide2):
    different = 0
    commun = 0
    tags_slide_1 = slide1.get_tags()
    tags_slide_2 = slide2.get_tags()

    for tag1 in tags_slide_1:
        for tag2 in tags_slide_2:
            if tag1 == tag2:
                commun += 1
            else:
                different += 1

    return different, commun


def max_common_tags_slides(slide1, other_slides):
    slideMax = -1
    max = 0

    for slide in other_slides:
        if compare_two_slides(slide1, slide)[1] > max:
            slideMax = slide
            max = len(slideMax.get_tags())

    return slide1, slideMax, max


def min_common_tags_slides(slide1, other_slides):
    slideMin = -1
    min = 200000

    for slide in other_slides:
        if compare_two_slides(slide1, slide)[1] < min:
            slideMin = slide
            min = len(slideMin.get_tags())

    return slide1, slideMin, min


def max_different_tags_slides(slide1, other_slides):
    slideMax = -1
    max = 0

    for slide in other_slides:
        if compare_two_slides(slide1, slide)[0] > max:
            slideMax = slide
            max = len(slideMax.get_tags())

    return slide1, slideMax, max


def min_different_tags_slides(slide1, other_slides):
    slideMin = -1
    min = 200000

    for slide in other_slides:
        if compare_two_slides(slide1, slide)[0] < min:
            slideMin = slide
            min = len(slideMin.get_tags())

    return slide1, slideMin, min


def max_common_tags_photos(photo1, other_photos):
    photoMax = -1
    max = 0

    for photo in other_photos:
        if compare_two_photos(photo1, photo)[1] > max:
            photoMax = photo
            max = len(photoMax.get_tags())

    return photo1, photoMax, max


def min_common_tags_photos(photo1, other_photos):
    photoMin = -1
    min = 0

    for photo in other_photos:
        if compare_two_photos(photo1, photo)[1] < min:
            photoMin = photo
            min = len(photoMin.get_tags())

    return photo1, photoMin, min


def max_different_tags_photos(photo1, other_photos):
    photoMax = -1
    max = 0

    for photo in other_photos:
        if compare_two_photos(photo1, photo)[0] > max:
            photoMax = photo
            max = len(photoMax.get_tags())

    return photo1, photoMax, max


def min_different_tags_photos(photo1, other_photos):
    photoMin = -1
    min = 0

    for photo in other_photos:
        if compare_two_photos(photo1, photo)[0] < min:
            photoMin = photo
            min = len(photoMin.get_tags())

    return photo1, photoMin, min



# FAITES VOS TESTS ICI SI BESOIN
if __name__ == "__main__":
    print()
    print(smart_algo(parseFile("assignment/e_shiny_selfies.txt")))

