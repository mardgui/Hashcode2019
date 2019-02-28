import time, sys, random


def get_non_empty_lines(filename):
    try:
        lines = [line.strip() for line in open(filename, "r")]
        lines = [line for line in lines if line]  # Skipping blank lines
        l = len(lines)
        return l, lines
    except IOError as e:
        print("Unable to read output file!\n" + e)
        return []


def do_stuff():
    t1 = time.time()
    length, lines = get_non_empty_lines(sys.argv[1])
    r = random.randrange(length)
    print(lines[r])
    print(time.time() - t1)


# run with test-file.txt as argument to test it, i.e. "python3 main.py test-file.txt"

if __name__ == "__main__":
    do_stuff()
