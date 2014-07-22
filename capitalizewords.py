# Program to capitalize first letter for each word in a sentence

import sys

if __name__ == '__main__':

    with open(sys.argv[1]) as fp:
        for line in fp:
            line = line.strip().split()
            print " ".join([word[0].upper()+word[1:] for word in line ])



