import sys

def happy(n):
    res = []
    while n not in res and n!=1:
        res.append(n)
        n = sum([int(i)**2 for i in str(n)])
        # res.append(n)
    return 0 if n!=1 else 1


def test():
    assert happy(1) == 1
    assert happy(7) == 1
    assert happy(22) == 0
    print "All test cleared"

if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        for line in fp:
            print happy(int(line.strip()))

    fp.close()

    # test()
