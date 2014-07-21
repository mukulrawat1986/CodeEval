import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        for line in fp:
            print int(line.strip(), 16)
    fp.close()
