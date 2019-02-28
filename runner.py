import sys

import photos_base


def score(file_in, file_out):
    lines_in = [line.strip() for line in open(file_in, "r")]
    lines_out = [line.strip() for line in open(file_out, "r")]

    photo_tags = [line.split(' ')[2:] for line in lines_in[1:]]

    def interest_factor(slide_1, slide_2):
        tags_1 = set()
        tags_2 = set()
        for photo in slide_1.split(' '):
            for tag in photo_tags[int(photo)]:
                tags_1.add(tag)
        for photo in slide_2.split(' '):
            for tag in photo_tags[int(photo)]:
                tags_2.add(tag)

        return min(len(tags_1 - tags_2), len(tags_2 - tags_1), len(tags_1 & tags_2))

    total_score = 0

    for i in range(1, len(lines_out) - 1):
        total_score += interest_factor(lines_out[i], lines_out[i + 1])

    return total_score


if __name__ == "__main__":
    files = ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']
    for i, file in enumerate(files):
        files[i] = 'assignment/' + file + '.txt'

    for file in files:
        sys.stdout = open('out_{}'.format(file[11:]), 'w')
        photos_base.smart_algo(photos_base.parseFile_v2(file))
        #photos_base.random_algo(file)
    sys.stdout = sys.__stdout__

    scores = []
    for file in files:
        scores.append( score(file, 'out_{}'.format(file[11:])))
        print('Score on file {}: {}'.format(file[11:], scores[-1]))

    print('Total score: {}'.format(sum(scores)))
