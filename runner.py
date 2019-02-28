import sys

import photos_base


def score(file_in, file_out):
    file_in = open(file_in, 'r')
    file_out = open(file_out, 'r')

    photosDesc = {}
    cpt = 0
    for i in file_in:
        line = i.replace("\n", "").split(" ")
        photosDesc[cpt] = line[2:]
        cpt += 1
    # print(photosDesc)

    cpt = 0
    prevTags = []
    tags = []
    totalScore = 0

    for i in file_out:
        prevTags = tags
        tags = []
        common = 0
        different1 = 0
        different2 = 0

        line = i.replace("\n", "").split(" ")
        tags.append(photosDesc[int(line[0])])
        if len(line) > 1:
            tags.append(photosDesc[int(line[1])])

        if cpt == 0:
            cpt += 1
            continue

        for x in tags:
            for y in x:
                for z in prevTags:
                    if y in z:
                        common += 1
                    else:
                        different1 += 1

        for x in prevTags:
            for y in x:
                for z in tags:
                    if y not in z:
                        different2 += 1

        totalScore += min(common, different1, different2)

    return totalScore


if __name__ == "__main__":
    files = ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']
    for i, file in enumerate(files):
        files[i] = 'assignment/' + file + '.txt'

    for file in files:
        sys.stdout = open('out_{}'.format(file[11:]), 'w')
        photos_base.random_algo(file)

    sys.stdout = sys.__stdout__

    for file in files:
        print('Score on file {}: {}'.format(file[11:], score(file, 'out_{}'.format(file[11:]))))
