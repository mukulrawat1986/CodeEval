import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as fp:
        for line in fp:
            li = line.strip().split()
            print sorted(li, reverse = True, key = lambda x: len(x))[0]
    fp.close()
