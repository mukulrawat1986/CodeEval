

import sys

if __name__ == "__main__":

    filename = sys.argv[1]
    with open(filename) as fp:

        for line in fp:
            print " ".join(line.split()[::-1])


    fp.close()
