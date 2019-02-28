import sys

import photos_base

if __name__ == "__main__":
    files = ['a_example', 'b_lovely_landscapes', 'c_memorable_moments', 'd_pet_pictures', 'e_shiny_selfies']
    for i, file in enumerate(files):
        files[i] = 'assignment/' + file + '.txt'

    for file in files:
        sys.stdout = open('out_{}'.format(file[11:]), 'w')
        photos_base.random_algo(file)
