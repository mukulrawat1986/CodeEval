import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        for line in fp:
            res = all([line.count(str(x)) == int(y) for x,y  in enumerate(line.strip())])
            print int(res)

    fp.close()
